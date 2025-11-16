from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Base directory = folder info/111 where this file lives
BASE_DIR = Path(__file__).resolve().parent


def make_figure_1_radar_articles() -> Path:
    """
    Figure 1.
    Conceptual radar chart comparing key features of Articles 111 and 111-1 CCU.
    """

    labels = [
        "Object of\nprotection",
        "Subject",
        "Breadth of\nconduct",
        "Level of\nharm",
        "Link to\nterritory",
    ]

    # Conceptual (subjective) scores 1–5 for illustration
    art_111 = [5, 5, 3, 5, 4]   # High treason
    art_111_1 = [4, 3, 5, 3, 5]  # Collaboration

    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    v_111 = np.concatenate((art_111, [art_111[0]]))
    v_111_1 = np.concatenate((art_111_1, [art_111_1[0]]))

    fig, ax = plt.subplots(subplot_kw=dict(polar=True), figsize=(8, 6))

    ax.plot(angles, v_111, marker="o", label="Art. 111 (high treason)")
    ax.fill(angles, v_111, alpha=0.25)

    ax.plot(angles, v_111_1, marker="o", label="Art. 111-1 (collaboration)")
    ax.fill(angles, v_111_1, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)

    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
    ax.set_ylim(0, 5)

    ax.set_title("Conceptual comparison of Articles 111 and 111-1 CCU", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.4, 1.1))

    fig.tight_layout()
    path = BASE_DIR / "fig_111_radar_articles.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return path


def make_figure_2_mice_rascls_map() -> Path:
    """
    Figure 2.
    Bipartite map of links between MICE and RASCLS components.
    """
    mice = ["Money", "Ideology", "Coercion/\nCompromise", "Ego"]
    rascls = ["Reciprocation", "Authority", "Scarcity",
              "Commitment/\nConsistency", "Liking", "Social proof"]

    mice_x = [0] * len(mice)
    mice_y = list(range(len(mice)))
    ras_x = [5] * len(rascls)
    ras_y = list(range(len(rascls)))

    fig, ax = plt.subplots(figsize=(9, 6))

    # Nodes
    ax.scatter(mice_x, mice_y, s=400)
    ax.scatter(ras_x, ras_y, s=400)

    for x, y, label in zip(mice_x, mice_y, mice):
        ax.text(x - 0.1, y, label, ha="right", va="center", fontsize=10)

    for x, y, label in zip(ras_x, ras_y, rascls):
        ax.text(x + 0.1, y, label, ha="left", va="center", fontsize=10)

    # Links (you can extend them later)
    connections = [
        ("Money", "Reciprocation"),
        ("Money", "Scarcity"),
        ("Ideology", "Authority"),
        ("Ideology", "Social proof"),
        ("Coercion/\nCompromise", "Scarcity"),
        ("Coercion/\nCompromise", "Commitment/\nConsistency"),
        ("Ego", "Liking"),
        ("Ego", "Authority"),
    ]

    def get_coords(name: str):
        if name in mice:
            idx = mice.index(name)
            return mice_x[idx], mice_y[idx]
        idx = rascls.index(name)
        return ras_x[idx], ras_y[idx]

    for left, right in connections:
        x1, y1 = get_coords(left)
        x2, y2 = get_coords(right)
        ax.plot([x1, x2], [y1, y2], alpha=0.7)

    ax.set_title("Links between MICE motivations and RASCLS influence tools")
    ax.axis("off")

    fig.tight_layout()
    path = BASE_DIR / "fig_111_mice_rascls_map.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return path


def make_figure_3_flow_factors() -> Path:
    """
    Figure 3.
    Schematic flow:
    Factors → motivational mechanisms (MICE, RASCLS) → legal qualification.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Nodes: factors, MICE, RASCLS, articles
    factors = [
        ("Ideology /\npolitical\nloyalty", (1, 7)),
        ("Money /\nbenefit", (1, 5)),
        ("Coercion /\ncompromise", (1, 3)),
        ("Placement /\naccess", (1, 1)),
    ]

    mice_nodes = [
        ("MICE:\nIdeology", (4, 7.5)),
        ("MICE:\nMoney", (4, 5.5)),
        ("MICE:\nCoercion/\nCompromise", (4, 3.5)),
        ("MICE:\nEgo", (4, 1.5)),
    ]

    rascls_nodes = [
        ("RASCLS:\nAuthority", (7, 8)),
        ("RASCLS:\nReciprocation", (7, 6.5)),
        ("RASCLS:\nScarcity", (7, 5)),
        ("RASCLS:\nCommitment/\nConsistency", (7, 3.5)),
        ("RASCLS:\nLiking", (7, 2)),
        ("RASCLS:\nSocial proof", (7, 0.8)),
    ]

    articles = [
        ("Art. 111\n(high treason)", (9.5, 6)),
        ("Art. 111-1\n(collaboration)", (9.5, 3)),
    ]

    def draw_box(text: str, xy):
        ax.text(
            xy[0],
            xy[1],
            text,
            ha="center",
            va="center",
            fontsize=8,
            bbox=dict(boxstyle="round,pad=0.4", alpha=0.2),
        )

    for text, pos in factors + mice_nodes + rascls_nodes + articles:
        draw_box(text, pos)

    def arrow(from_xy, to_xy):
        ax.annotate(
            "",
            xy=to_xy,
            xytext=from_xy,
            arrowprops=dict(arrowstyle="->", alpha=0.6),
        )

    names_to_pos = {
        text: pos for text, pos in factors + mice_nodes + rascls_nodes + articles
    }

    # Factor → MICE/RASCLS links
    links = [
        ("Ideology /\npolitical\nloyalty", "MICE:\nIdeology"),
        ("Ideology /\npolitical\nloyalty", "MICE:\nEgo"),
        ("Ideology /\npolitical\nloyalty", "RASCLS:\nAuthority"),
        ("Ideology /\npolitical\nloyalty", "RASCLS:\nSocial proof"),
        ("Money /\nbenefit", "MICE:\nMoney"),
        ("Money /\nbenefit", "RASCLS:\nReciprocation"),
        ("Money /\nbenefit", "RASCLS:\nScarcity"),
        ("Coercion /\ncompromise", "MICE:\nCoercion/\nCompromise"),
        ("Coercion /\ncompromise", "RASCLS:\nScarcity"),
        ("Placement /\naccess", "MICE:\nEgo"),
        ("Placement /\naccess", "RASCLS:\nCommitment/\nConsistency"),
    ]

    for a, b in links:
        arrow(names_to_pos[a], names_to_pos[b])

    # MICE/RASCLS → articles (simplified)
    mech_nodes = [name for name, _ in mice_nodes + rascls_nodes]
    article_nodes = [name for name, _ in articles]

    for mech in mech_nodes:
        for art in article_nodes:
            arrow(names_to_pos[mech], names_to_pos[art])

    ax.set_title(
        "Factors → motivational mechanisms (MICE, RASCLS) → legal qualification"
    )

    fig.tight_layout()
    path = BASE_DIR / "fig_111_flow_factors_mice_rascls.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return path


def make_dataset() -> pd.DataFrame:
    """
    Build a small, case-based dataset for Variant B.

    The values are manual 0/1 codings of factors for the real case:
    MP Oleksandr Dubinsky, who in November 2023 was notified of suspicion
    of high treason (Art. 111 CCU) in connection with an alleged GRU-linked
    influence network (based on open-source media reports, e.g. Suspilne).

    IMPORTANT:
    - This is an analytical / educational coding, not a judicial fact.
    - Presumption of innocence applies.
    """

    data = [
        {
            "case": "Oleksandr Dubinsky",
            "type": "Member of Parliament / media figure",
            # MICE
            "Money": 1,
            "Ideology": 1,
            "Coercion": 0,
            "Ego": 1,
            # RASCLS
            "Reciprocation": 1,
            "Authority": 1,
            "Scarcity": 0,
            "Commitment": 1,
            "Liking": 0,
            "SocialProof": 1,
            # Legal article (suspicion)
            "article": "111",
        }
    ]

    return pd.DataFrame(data)


def make_figure_4_factor_frequency(df: pd.DataFrame) -> Path:
    """
    Figure 4.
    Frequency of motivational factors / influence tools (bar chart).
    In this pilot dataset, it is simply the 0/1 profile of one real case.
    """

    factors_cols = [
        "Money",
        "Ideology",
        "Coercion",
        "Ego",
        "Reciprocation",
        "Authority",
        "Scarcity",
        "Commitment",
        "Liking",
        "SocialProof",
    ]

    factor_counts = df[factors_cols].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    factor_counts.plot(kind="bar", ax=ax)

    ax.set_ylabel("Number of cases where factor is present")
    ax.set_title("Frequency of motivational factors (pilot dataset based on Dubinsky case)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    fig.tight_layout()
    path = BASE_DIR / "fig_111_bar_factor_frequency.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return path


def make_figure_5_mice_by_type(df: pd.DataFrame) -> Path:
    """
    Figure 5.
    MICE profile by actor type.

    With one case we only get one bar-group ("Member of Parliament / media figure"),
    but the code is ready to handle more types if new cases are added later.
    """

    selected = df[["type", "Money", "Ideology", "Coercion", "Ego"]]
    grouped = selected.groupby("type").mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)

    ax.set_ylabel("Average value (0–1)")
    ax.set_title("MICE profile by actor type (pilot dataset)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.legend(title="Factor")

    fig.tight_layout()
    path = BASE_DIR / "fig_111_bar_mice_by_type.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return path


def make_figure_6_radar_profiles_by_article(df: pd.DataFrame) -> Path:
    """
    Figure 6.
    Radar chart of factor profiles by article (111 / 111-1).

    Currently the dataset only contains one real case under Art. 111,
    so only that profile appears. If you later add coded Art. 111-1
    cases, the same function will automatically plot both.
    """

    factors_cols = [
        "Money",
        "Ideology",
        "Coercion",
        "Ego",
        "Reciprocation",
        "Authority",
        "Scarcity",
        "Commitment",
        "Liking",
        "SocialProof",
    ]

    group_by_article = df.groupby("article")[factors_cols].mean()

    labels = factors_cols
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    fig, ax = plt.subplots(subplot_kw=dict(polar=True), figsize=(8, 6))

    def add_series(values: np.ndarray, label: str):
        vals = np.concatenate((values, [values[0]]))
        ax.plot(angles, vals, marker="o", label=label)
        ax.fill(angles, vals, alpha=0.25)

    if "111" in group_by_article.index:
        add_series(group_by_article.loc["111"].values, "Art. 111 (high treason)")

    if "111-1" in group_by_article.index:
        add_series(group_by_article.loc["111-1"].values, "Art. 111-1 (collaboration)")

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=8, rotation=45)

    ax.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0", "0.25", "0.5", "0.75", "1.0"], fontsize=7)
    ax.set_ylim(0, 1.0)

    ax.set_title("Factor profiles by article (pilot dataset)", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.4, 1.1))

    fig.tight_layout()
    path = BASE_DIR / "fig_111_radar_profiles_by_article.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return path


def main() -> None:
    # Ensure folder exists
    BASE_DIR.mkdir(exist_ok=True, parents=True)

    # Variant A: conceptual schemes
    make_figure_1_radar_articles()
    make_figure_2_mice_rascls_map()
    make_figure_3_flow_factors()

    # Variant B: case-based dataset and charts
    df = make_dataset()
    make_figure_4_factor_frequency(df)
    make_figure_5_mice_by_type(df)
    make_figure_6_radar_profiles_by_article(df)

    print("All figures saved to:", BASE_DIR)


if __name__ == "__main__":
    main()
