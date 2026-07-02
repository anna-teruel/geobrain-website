

# GeoBrain

**GeoBrain** is an interactive Python framework for visualizing atlas-based quantitative histological data on the Allen Mouse Brain Common Coordinate Framework (CCFv3).

Modern image analysis pipelines such as [QUINT](https://quint-workflow.readthedocs.io/en/latest/index.html) generate region-level measurements across the entire brain, including object counts, densities, frequencies, and other quantitative metrics. While these workflows provide robust quantification, the resulting data are typically distributed as large tables that can be difficult to interpret spatially.

GeoBrain bridges this gap by transforming region-wise measurements into interactive anatomical visualizations. The framework maps quantitative metrics onto 2D atlas representations, enabling intuitive exploration of brain-wide spatial patterns across coronal, sagittal, and horizontal planes.

Unlike traditional single-sample visualization tools, GeoBrain is designed for cohort-level analysis. It supports the integration of data across multiple animals and experimental groups, allowing users to visualize population-level metrics and compare spatial distributions between conditions.

Built on Plotly, GeoBrain provides:

* Interactive atlas navigation across multiple anatomical planes.
* Visualization of region-level metrics such as frequency, density, and relative abundance.
* Cohort and group comparisons.
* Customizable color mapping and scaling.
* Web-based dashboards for exploratory analysis.
* Publication-quality figure export.


Use the navigation menu to explore installation instructions, tutorials, examples, and the API reference.


```{toctree}
:maxdepth: 2
:caption: User guides

user_guides
```

```{toctree}
:maxdepth: 2
:caption: Examples

examples
```

```{toctree}
:maxdepth: 2
:caption: Community

community
```

```{toctree}
:maxdepth: 2
:caption: API reference

api
```