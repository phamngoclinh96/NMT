#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
import argparse

from onmt.translate.Translator import make_translator
from onmt.Utils import get_logger

import onmt.io
import onmt.translate
import onmt
import onmt.ModelConstructor
import onmt.modules
import onmt.opts


def main(opt):
    translator = make_translator(opt, report_score=True, logger=logger)
    translator.translate(opt.src_dir, opt.src, opt.tgt,
                         opt.batch_size, opt.attn_debug)


if __name__ == "__main__":
    import en_core_web_sm
    tokenizer = en_core_web_sm.load()
    parser = argparse.ArgumentParser(
        description='translate.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    onmt.opts.add_md_help_argument(parser)
    onmt.opts.translate_opts(parser)

    opt = parser.parse_args()
    opt.src = 'test/test.en'
    opt.model = 'en_vi/model/2706.en_vi_acc_44.19_ppl_26.01_e7.pt'
    opt.output = 'test/test.vi'
    opt.replace_unk = True
    logger = get_logger(opt.log_file)
    lines = open(opt.src,'r',encoding='utf-8').readlines()
    tmp = 'test/tmp/src.txt'
    writer = open(tmp,'w',encoding='utf-8')
    for line in lines:
        line = tokenizer(line)
        writer.write(' '.join([token.text for token in line]))
    writer.close()
    opt.src = tmp
    main(opt)

# python translate.py -model en_vi/model/en_vi_acc_41.75_ppl_24.91_e7.pt -src en_vi/test/test.en -output en_vi/test/test.vi -replace_unk -verbose
