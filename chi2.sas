libname data_set "SAS_Data";

data data_set.speech_imp;
  input Sex $ Speech $ count;
    datalines;
      Male Stammer 32
      Male Lisp 28
      Female Stammer 18
      Female Lisp 22
;
run;

proc report data = data_set.speech_imp;
  var:;
run;

proc freq data = data_set.speech_imp;
  tables Sex * Speech / chisq nocol norow nocum nopercent;
  weight count;
run;