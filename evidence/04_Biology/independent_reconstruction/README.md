# Independent reconstruction of the Biology viability-control models

`CU_Biology_reconstructed_reproducibility.py` was written by Claude (Opus 5.5) on 9 October 2026 from the written specification in the Biology technical supplement (§§B.2–B.7) alone, without access to the original script in `../C1_1_reproducibility_package/`.

It reproduces every published value in Supplement B to ten decimal places, including both coupling sweeps, the no-control reference failure (minimum margin −0.1009342470 at t = 26.76), and zero clipping. The output is in `CU_Biology_reconstructed_reproducibility_output.txt`.

Its purpose is to show that the paper specifies its model completely enough for an independent implementation to recover the reported numbers. The original script in `C1_1_reproducibility_package/` is the controlling evidence.
