<h2>Dihedral scan with xTB</h2>
<img src="https://github.com/gkxiao/xtb-scan/blob/main/fragment.png" align='middle' ">
<p style="text-align:center;">Figure 1. Example molecule. Highlighted dihedral: O8-C3-C2-C1</p>

<h3>1. Convert SDF into tmol:</h3>
<pre lang="python">
obabel -isdf 7jrn_ligand_fragment.sdf -otmol -O fragment.coord 
</pre>

<h3>2. Prepare input file: scan.inp</h3>
<pre lang="python">
$constrain
 force constant=50.0
 dihedral: 3,2,1,8,0.0
$scan
 1: 0.0,180.0,37
$end
</pre>

<h3>3. Perform torsion scan</h3>
<pre lang="python">
/public/apps/xtb-6.5.1/bin/xtb fragment.coord --opt verytight --input scan.inp --chrg 0 --uhf 0
</pre>

<h3>4. Convet xyz into sdf</h3>
<pre lang="python">
obabel -ixyz xtbscan.log -osdf -O xtbscan.sdf 
</pre>

<h3>5. Extract dihedral scan result:</h3>
<pre lang="python">
extract_result_from_xtbscan.py xtbscan.sdf 3 2 1 8
</pre>

<pre lang="python">
CONF_ID,Angle,Relative_energy
CONF_1,-0.0024379306925366028,2.5660529817770072
CONF_2,5.008868625895336,2.421691246670976
CONF_3,10.006264798942436,2.093297027544123
CONF_4,15.00388321707389,1.6735896340333944
CONF_5,20.00715882152012,1.2647560229912802
CONF_6,25.000484601098798,0.8956625742899149
CONF_7,30.007529505425715,0.58213106163155
CONF_8,35.004095113856685,0.33556458569846015
CONF_9,40.00801862447416,0.15920944683461613
CONF_10,45.00804589818885,0.05284170597375848
CONF_11,49.99270415026529,0.0
CONF_12,55.00734179011268,0.028588644606113434
CONF_13,60.000498933417326,0.12004189644131635
CONF_14,64.99456640846694,0.2535721908962252
CONF_15,69.99701297899928,0.4036983160734575
CONF_16,74.99655532565676,0.5444593369536221
CONF_17,80.00179918843254,0.673358565949691
CONF_18,85.00122039028727,0.77231599804092
CONF_19,89.9975075815823,0.8223022320087292
CONF_20,95.00738375966014,0.8516286609974788
CONF_21,100.00259993427802,0.8521607966847
CONF_22,104.99847953686145,0.8453869191246799
CONF_23,110.0011877780128,0.806081963800489
CONF_24,115.00441978156354,0.7774579526672376
CONF_25,119.9984682367587,0.77084727154201
CONF_26,125.00170760464812,0.7636051145771461
CONF_27,129.9950398843348,0.8105056405111188
CONF_28,134.99836088974644,0.9126517408357859
CONF_29,139.99480548215223,1.075909500156742
CONF_30,144.99631665389828,1.304110102778182
CONF_31,149.99225955738748,1.6134768207537142
CONF_32,154.99316032897417,1.9901157699614114
CONF_33,159.9907292258415,2.4379784477945154
CONF_34,164.99021865644528,2.9415040766211753
CONF_35,169.98836838604416,3.4729742068748326
CONF_36,174.98865151282774,3.9824196092070707
CONF_37,179.99766277109416,4.283353778243777
</pre>

<h3>6. Plot result</h3>
<img src="https://github.com/gkxiao/xtb-scan/blob/main/example.png" align='middle' />

<h2>Optimize conformer at DFT level with ORCA</h2>
<h3>7. Split conformer ensemble into single SDF/XYZ file</h3>
<p>Split the conformer ensemble into xyz file:</p>
<pre lang="python">
obabel -ixyz xtbscan.log -oxyz -O CONF_.xyz -m 
</pre>
<p>Split the conformer ensemble into sdf file:</p>
<pre lang="python">
obabel -ixyz xtbscan.xyz -osdf -O CONF_.sdf -m 
</pre>

<h3>8. Generate ORCA input file to optimize conformer with dihedral angle constrained</h3>
<p>Create ORCA input file from SDF:</p>
<pre lang="python">
sdf2orca CONF_1.sdf 8 2 3 1 CONF_1_opt.inp
</pre>
<p>Alterantively, create ORCA input file from XYZ:</p>
<pre lang="python">
xyz2orca CONF_1.xyz 0 8 2 3 1 CONF_1_opt.inp
</pre>
<h3>9. Perform optimization with ORCA at BP86-D3/DEF2-TZVP level</h3>
<pre lang="python">
orca CONF_1_opt.inp > CONF_1_opt.out
</pre>
<p>Chemistry model r2scan-3c/def2-mtzvpp and r2scan-3c/def2-tzvp is recommnnded.</p>
<h2>Reference</h2>
<ol>
   <li>User Guide to Semiempirical Tight Binding.<a href="https://xtb-docs.readthedocs.io/en/latest/">https://xtb-docs.readthedocs.io/en/latest</a></li>
   <li>ORCA tutorials. <a href="https://www.orcasoftware.de/tutorials_orca">ORCA tutorials - Compatible with ORCA 5.0!</a></li>
   <li>ORCA input library. <a href="https://sites.google.com/site/orcainputlibrary/">https://sites.google.com/site/orcainputlibrary</a></li>
   <li>M. Bursch, J.-M. Mewes, A. Hansen, S. Grimme. Best-Practice DFT Protocols for Basic Molecular Computational Chemistry. Angew. Chem. Int. Ed. 2022, 61, e202205735. https://doi.org/10.1002/anie.202205735 </li>
   <li>Grimme S, Hansen A, Ehlert S, Mewes J-M. <a href="https://chemrxiv.org/engage/chemrxiv/article-details/60c75338702a9b696218c304">r2SCAN-3c: An Efficient “Swiss Army Knife” Composite Electronic-Structure Method</a>. ChemRxiv. 2020; doi:10.26434/chemrxiv.13333520.v2 This content is a preprint and has not been peer-reviewed.</li>
   <li>Thomas Gasevic, Julius B. Stückrath, Stefan Grimme, and Markus Bursch.Optimization of the r2SCAN-3c Composite Electronic-Structure Method for Use with Slater-Type Orbital Basis Sets. The Journal of Physical Chemistry A 2022 126 (23), 3826-3838. DOI: 10.1021/acs.jpca.2c02951</li>
</ol>
