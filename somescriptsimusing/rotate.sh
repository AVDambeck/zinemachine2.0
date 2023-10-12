mkdir out; for i in *.jpg; do magick $i -rotate 180 out/$i; done;
