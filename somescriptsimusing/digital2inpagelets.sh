cd ~/Programs/zinemachine2.0;
cd infiles;
pdfseparate *.pdf img%02d.pdf;
for i in img*; do convert -density 300 -background white -alpha remove $i $(perl -e 'print $ARGV[0] =~ s/\.[^.]+$//r' $i).jpg; rm $i; done;
rm *.pdf;
cd ..;
rm inpagelets/*;
mv infiles/* inpagelets/;
