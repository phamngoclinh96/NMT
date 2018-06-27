



> python preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/data -src_vocab_size 1000 -tgt_vocab_size 1000

> python train.py -data data/data -save_model /n/rush_lab/data/tmp_ -gpuid 0 -rnn_size 100 -word_vec_size 50 -layers 1 -epochs 10 -optim adam  -learning_rate 0.001



python preprocess.py -train_src en_vi/data/train.en -train_tgt en_vi/data/train.vi -valid_src en_vi/data/tst2013.en -valid_tgt en_vi/data/tst2013.vi -save_data en_vi/data/data.en_vi -src_vocab_size 17191 -tgt_vocab_size 7709

python train.py -data en_vi/data/data.en_vi -save_model en_vi/model/en_vi -rnn_size 200 -word_vec_size 100 -layers 2 -epochs 10 -optim adam  -learning_rate 0.001

python translate.py -model en_vi/model/en_vi_acc_41.75_ppl_24.91_e7.pt -src en_vi/test/test.en -output en_vi/test/test.vi -replace_unk -verbose
