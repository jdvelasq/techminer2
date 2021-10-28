import matplotlib
import matplotlib.pyplot as plt


def lotka(core_authors, colormap="Greys", figsize=(8, 6), fontsize=11):

    data = core_authors.copy()
    percentage_authors = data["%"].map(lambda w: float(w[:-2])).tolist()
    documents_written = data["Documents written per Author"].tolist()

    matplotlib.rc("font", size=fontsize)
    fig, axs = plt.subplots(figsize=figsize)

    cmap = plt.cm.get_cmap(colormap)
    color = cmap(0.6)

    percentage_authors.reverse()
    documents_written.reverse()

    axs.plot(
        documents_written,
        percentage_authors,
        linestyle="-",
        linewidth=2,
        color="k",
    )
    axs.fill_between(
        documents_written,
        percentage_authors,
        color=color,
        alpha=0.6,
    )

    #
    # Theoretical
    #
    total_authors = data["Num Authors"].max()
    theoretical = [total_authors / float(x * x) for x in documents_written]
    total_theoretical = sum(theoretical)
    perc_theoretical_authors = [w / total_theoretical * 100 for w in theoretical]

    axs.plot(
        documents_written,
        perc_theoretical_authors,
        linestyle=":",
        linewidth=4,
        color="k",
    )

    for side in ["top", "right", "left", "bottom"]:
        axs.spines[side].set_visible(False)

    axs.grid(axis="y", color="gray", linestyle=":")
    axs.grid(axis="x", color="gray", linestyle=":")
    axs.set_ylabel("% of Authors")
    axs.set_xlabel("Documets written per Author")

    fig.set_tight_layout(True)
    return fig
