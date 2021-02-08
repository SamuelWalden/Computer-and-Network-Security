#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
\00\00\00\00\00\00\00\00uy\EE\83\E4ʅ&`1t\D9/T\D5A\AAT\FA\D3\FDvI\FA@\89(\E1X\CB\C8\ECR\B5\FDo\E6d"\F7\DF\91$'\CE<ˎm9\F7\B6\D7\E7\F2G\9B+\C7\E23y\9B\94\8BG\A711x&\84
 u@Vɗ\C1Uay\A2ŗ_\DEk:\97\B6\BFT\C0Ϙ\D6](\BEqU\AD,z!\9A\85\D66\C5-\F1\A9\D0
"""
from hashlib import sha256
if sha256(blob.encode('utf-8')).hexdigest() == '51a3a6165badd2c98637385554f9edea75010e606edc918fb037828d4c9e28fe':
	print("Hashing is not encryption!")

if sha256(blob.encode('utf-8')).hexdigest() == '3bb66baff5dae3106ff045fbb6aa9ae1ea49008b66d5d05c86ad2fce4103c9a4':
	print("Security through obscurity is snake-oil!")
print(sha256(blob.encode('utf-8')).hexdigest())



