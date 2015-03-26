Contains files that aren't necessary to the monte carlo, but help it evaluate a lot faster. 

There are a bunch of lightcurves for the F160W band, but I think these are still a little bit off, so it may be better to make them with SN Cosmo. 

The volumemag files contain arrays that have the lensed volume for magnifications of (1-100) for each of the 25 CLASH clusters. The ones that also have 'whalen' in the name are using the whalen cosmology, which was just a little different (the fiducial model I had was just omega_lambda = 0.7)

More volumemag files can be written using the volumemag.py program. Lightcurve files can be written using the lightcurve.py program. 
