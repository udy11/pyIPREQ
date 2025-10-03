# pyIPREQ

**Free-Boundary MHD Equilibrium Solver for Axisymmetric Tokamak**

This code solves Grad-Shafranov Equation for axisymmetric Tokamak plasma with given poloidal field coil and limiter configuration. The basic algorithm is based on this [article](https://doi.org/10.1016/0021-9991(79)90129-3).

Currently, a basic version of the code is available here. Other versions like plasma position constrained, betap constrained and inverse MHD Equilibrium solver will also be uploaded here soon.

To use the code, open the ipynb file using the Jupyter Notebook/Lab. The required Python-3 libraries are numpy, scipy, matplotlib, scikit-image and shapely. I expect the code to work with the latest version of these libraries, so if you encounter an issue please let me know.

If you used this code for your research, please cite this repository and the following article: [https://doi.org/10.1063/5.0290301](https://doi.org/10.1063/5.0290301). This article is also available on [arXiv](https://arxiv.org/abs/2507.18324).

Critical updates coming soon:
- A more robust algorithm to find psi surfaces, the current one might fail in some cases.
- A faster computation of Green's functions using Lackner and Von Hagenow formulation.

For any feedback, query or discussion, please contact me on [email](mailto:udaya_cbscients@yahoo.com) or [Telegram](https://t.me/udy11). If any of my work has been useful to you and you would like to donate cryptocurrencies, please click [here](https://github.com/udy11/udy11/blob/main/Donate_Crypto.md) or [here](https://gitlab.com/udy11/udy11/-/blob/main/Donate_Crypto.md). Thanks for visiting :)
