import matplotlib.pyplot as plt
import pandas as pd


# def annotate_plot(ax, xlab=None, ylab=None, title=None, legend_title=None, x_y_fontsize=None, subplot_top_adjustment=None, xticklabels=None):
#     ax.set_xlabels(xlab, fontsize=x_y_fontsize)
#     ax.set_ylabels(ylab, fontsize=x_y_fontsize)
#     ax.fig.subplots_adjust(top=subplot_top_adjustment)
#     ax._legend.set_title(legend_title)
#     ax.fig.suptitle(title)
#     ax.set_xticklabels(xticklabels)
#     # plt.show()


# def summarize_data(df):
#     print(f"Dataframe has {df.shape[1]} Columns and {df.shape[0]} Rows")
#     print(f"{'*' * 100}")
#     null_summary = pd.DataFrame(df.isnull().sum())
#     null_summary.columns = ["Number of Missing Values"]
#     null_summary["% Missing"] = round(100 * null_summary["Number of Missing Values"] /
#                                       len(df), 2)
#     print(
#         f"Number of Missing Values and % Missing Values per Column:\n{null_summary}")


def annotate_count_plot(g, kind=None):
    # Annotate the bars with the count at the top of each bar
    # iterate through axes
    if kind == 'percent':
        # Annotate the bars with the count at the top of each bar
        # iterate through axes
        for ax in g.axes.ravel():
            # add annotations
            for c in ax.containers:
                labels = [f'{round(100 * v.get_height(),2)} %' for v in c]
                ax.bar_label(c, labels=labels, label_type='edge')
            ax.margins(y=0.2)
    else:
        for ax in g.axes.ravel():
            # add annotations
            for c in ax.containers:
                labels = [f'{v.get_height()}' for v in c]
                ax.bar_label(c, labels=labels, label_type='edge')
            ax.margins(y=0.2)
