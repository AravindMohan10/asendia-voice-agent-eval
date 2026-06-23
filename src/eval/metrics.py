"""Eval metrics — accuracy, precision, recall, ECE calibration."""

from __future__ import annotations

from dataclasses import dataclass

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


@dataclass
class EvalMetrics:
    n: int
    accuracy: float
    precision_select: float
    recall_select: float
    f1_select: float
    ece: float
    high_confidence_error_rate: float


def expected_calibration_error(
    y_true: list[int],
    y_conf: list[float],
    n_bins: int = 10,
) -> float:
    """ECE for binary outcomes. y_true: 0/1, y_conf: predicted confidence for positive class."""
    confidences = np.array(y_conf)
    accuracies = np.array(y_true)
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = bins[i], bins[i + 1]
        mask = (confidences > lo) & (confidences <= hi)
        if mask.sum() == 0:
            continue
        bin_acc = accuracies[mask].mean()
        bin_conf = confidences[mask].mean()
        ece += mask.sum() / len(confidences) * abs(bin_acc - bin_conf)
    return float(ece)


def compute_metrics(
    y_true: list[str],
    y_pred: list[str],
    confidences: list[int],
    confidence_threshold: int = 80,
) -> EvalMetrics:
    labels = ["reject", "select"]
    y_t = [1 if y == "select" else 0 for y in y_true]
    y_p = [1 if y == "select" else 0 for y in y_pred]

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_t, y_p, average="binary", pos_label=1, zero_division=0
    )

    # Confidence for predicted class (0-1 scale)
    conf_for_pred = []
    for pred, conf in zip(y_pred, confidences):
        conf_for_pred.append(conf / 100.0 if pred == "select" else (100 - conf) / 100.0)

    correct = [1 if t == p else 0 for t, p in zip(y_t, y_p)]
    high_conf_wrong = [
        1
        for c, ok, conf in zip(y_pred, correct, confidences)
        if conf >= confidence_threshold and ok == 0
    ]
    high_conf_total = sum(1 for conf in confidences if conf >= confidence_threshold)
    hce_rate = len(high_conf_wrong) / high_conf_total if high_conf_total else 0.0

    return EvalMetrics(
        n=len(y_true),
        accuracy=float(accuracy_score(y_t, y_p)),
        precision_select=float(precision),
        recall_select=float(recall),
        f1_select=float(f1),
        ece=expected_calibration_error(correct, conf_for_pred),
        high_confidence_error_rate=float(hce_rate),
    )


def plot_calibration(
    y_true: list[str],
    y_pred: list[str],
    confidences: list[int],
    out_path: str,
    n_bins: int = 10,
) -> None:
    correct = [1 if t == p else 0 for t, p in zip(y_true, y_pred)]
    conf_for_pred = [
        c / 100.0 if p == "select" else (100 - c) / 100.0
        for p, c in zip(y_pred, confidences)
    ]

    bins = np.linspace(0, 1, n_bins + 1)
    bin_centers, bin_accs = [], []

    for i in range(n_bins):
        lo, hi = bins[i], bins[i + 1]
        mask = [(lo < c <= hi) for c in conf_for_pred]
        if not any(mask):
            continue
        acc = np.mean([correct[j] for j, m in enumerate(mask) if m])
        conf = np.mean([conf_for_pred[j] for j, m in enumerate(mask) if m])
        bin_centers.append(conf)
        bin_accs.append(acc)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot([0, 1], [0, 1], "k--", label="Perfect calibration")
    ax.scatter(bin_centers, bin_accs, s=80, zorder=3, label="Agent")
    ax.plot(bin_centers, bin_accs, alpha=0.6)
    ax.set_xlabel("Confidence")
    ax.set_ylabel("Accuracy")
    ax.set_title("Confidence Calibration (Reliability Diagram)")
    ax.legend()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
