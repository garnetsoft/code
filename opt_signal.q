
{
 tickers:("SS";enlist",") 0: `:/home/ubuntu/data/iexq/sp100.csv;
 opt2:raze {
  d:ssr[string y;".";""];
  f:"" sv (":/tmp/";upper(string x);"_put_call_ratio",d,".csv");
  t:("SSFDDIIFFFF";enlist",")0:hsym `$f;
  t
  }[;.z.D-1] each lower[exec distinct Symbol from tickers];

 t:`bear2bullRatioAbs xdesc 
 update bear2bullRatio:bearish%bull, bear2bullRatioAbs:abs log(bearish%bull) from 
 exec `bearish`bull`#(signal!dollarValue) by sym:symbol from 
 select count i, sum volume, sum dollarValue by symbol, signal from 
 update signal:?[not closingPrice within(bid;ask);`;signal] from
 update signal:{s:();
   if[(x=`call) and (y=`buyOpt);s:`bull]; if[(x=`put) and (y=`sellOpt);s:`bull];
   if[(x=`call) and (y=`sellOpt);s:`bearish]; if[(x=`put) and (y=`buyOpt);s:`bearish];
   s }'[side;optSide] from 
 update optSide:?[closingPrice<0.5*(bid+ask);`sellOpt;`buyOpt] from
 select from opt2;

 `bear2bullRatio xdesc select from t where bearish>1000000,bull>1000000
 }[] 

