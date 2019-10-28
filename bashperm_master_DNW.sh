#! /bin/bash
### This script performs permutations on random data
### Written by Grace Bottum, October 2015
### Modified by Dominique Neitzel Wagner, January 2016
### It requires script rand_ind_master.py to be in the same directory
### To silence console, run "bashperm_all.sh &> /dev/null"

for file in *.vcf ## VCF with individuals and genotypes
do
	for run in {1..1000} ## Change {1..100} to any number of permutations i.e. {1..500}
	do
		OUTPUT=$(python rand_ind_master_DNW.py) ### Run your python script to randomize samples
		
		### Now run the test on randomized groups
		vcftools --vcf $file --weir-fst-pop Atest.txt --weir-fst-pop Btest.txt --out mktemp
		awk 'BEGIN{FS="\t"}{getline f1 <"FstVal.txt" ;print f1,$3}' OFS="\t" mktemp.weir.fst > tmptxt.txt
		mv tmptxt.txt FstVal.txt
	done
	> fst_$file.txt
	mv FstVal.txt fst_$file.txt
done
