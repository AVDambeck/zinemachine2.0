for i in `ls inpagelets/`; do convert inpagelets/$i util/cache/$i.pdf; done;
pdfunite util/cache/* DIGITAL.pdf;
rm util/cache/*;

