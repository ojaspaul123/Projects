
# 🧢 Jockey Distribution Report 2024
### Complete Data Analysis & Visualization using Python

---
This notebook is a sales distribution analysis report for Jockey India (2024), built for a distributor named Chirag Paul. It loads order-level transaction data (ChiragPaul_Jockey_Distributor_2024.csv) covering products, retailers, quantities, pricing, invoices, GST, and payment details.
The pipeline: cleans the data (missing values, type conversion, deduplication), filters for fulfilled/unpaid/high-value/Q4 orders, engineers new features (delivery days, fulfillment rate, profit margin, revenue bands), then produces 20+ visualizations across Matplotlib, Seaborn, and Plotly — covering monthly revenue trends, top retailers, section-wise performance, heatmaps, payment status breakdowns, and an interactive Sunburst/Treemap/Funnel. The final cleaned CSV is exported.

🐛 Bugs Fixed (3)
#LocationBugFix1mpl-bar2 (MPL-2)ax1.legend([b1, b2], ...) passes raw BarContainer objects — legend shows blank entriesReplaced with ax1.get_legend_handles_labels() + ax2.get_legend_handles_labels() combined2mpl-scatter (MPL-8)plt.cm.get_cmap('tab10', len(sections)) — deprecated in Matplotlib 3.7+, raises warning/errorReplaced with plt.colormaps.get_cmap('tab10')3sns-violin (SNS-4)inner='quartile' is not a valid seaborn violinplot value — causes ValueErrorCorrected to inner='quart' (the valid seaborn parameter)

