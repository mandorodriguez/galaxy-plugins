#!/bin/bash                                                                                                                                                                     

source /gdata/anaconda3/conda-env.sh
conda activate mgefinder


SEQFILE=$1
SENSITIVE_MODE=$2
MODE=$3

sensitive=""
if [ "$SENSITIVE_MODE" == "1" ]l then
    sensitive="--sensitive"
fi


echo "The options passed are $@"
CMD=`which mgefinder`
echo "Command is $CMD"



conda deactivate
echo "MGEfinder done"
