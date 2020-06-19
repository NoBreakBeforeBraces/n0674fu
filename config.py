from collections import OrderedDict

nid = 'syosetu_n0674fu'

title = '观察力太好的我不放过毒舌冷娇美少女任何娇羞之处，不断地对她进行攻略'

description = """笹原直哉在某一天出手相救了同级的女生白金小雪，使她免于恶质的搭讪。

她在学校里被称作『剧毒的白雪公主』，是有名的超绝美少女（毒舌）。
从那天开始，直哉似乎就被小雪不停地缠上了……。

「哎呀哎呀，日安，笹原君。今天你也是一个人放学回家吗。明明朋友们全~都去陪女朋友了，只有你一个人孤零零的，真是寂寞的青春呢？」
「原来如此，简而言之就是『笹原君居然是一个人耶Lucky！可不可以和他一起走啊……但我又没勇气主动开口……』对吧。好啊，一起回去吧。」
「什、你想多……没这回事，不，也不能说完全没这回事……！」

这是一个，察言观色能力超强的主人公毫不放过冷娇少女的所有娇羞时刻，一个劲地对她发动恋爱攻势的故事。

※现在不定期更新中
※男主角跟小雪之外的任何女人都不会有哪怕半支旗子产生
"""

author = "ふか田さめたろう"

menu = OrderedDict()
# 将range后括号内后一个数字设置为已翻译完成话数+1
menu["序章"] = [f'{i:0>4}.tex' for i in range(1, 7)]
# menu["第一章"] = [f'{i:0>4}.tex' for i in range(8, 8)]
# menu["第二章"] = [f'{i:0>4}.tex' for i in range(20, 20)]
# menu["第三章"] = [f'{i:0>4}.tex' for i in range(28, 28)]
# menu["第四章"] = [f'{i:0>4}.tex' for i in range(36, 36)]
# menu["第五章"] = [f'{i:0>4}.tex' for i in range(50, 50)]
# menu["番外篇"] = [f'{i:0>4}.tex' for i in range(60, 60)]
# menu["第六章"] = [f'{i:0>4}.tex' for i in range(62, 62)]
# menu["第七章"] = [f'{i:0>4}.tex' for i in range(72, 72)]

masiro_forum_id = 330
masiro_menu_thread_type = 3977

sub_characters = None

_masiro_thread_type_map = {
    "番外篇": 3980,
    "序章": 3983,
    "第一章": 3984,
    "第二章": 3985,
    "第三章": 3986,
    "第四章": 3987,
    "第五章": 3988,
    "第六章": 3989,
    "第七章": 3990,
    "第八章": 3992,
    "第九章": 3993,
    "第十章": 3994,
    "第十一章": 3995,
    "第十二章": 3996,
    "第十三章": 3997,
}
masiro_thread_type = lambda section_title, file: _masiro_thread_type_map[section_title]
masiro_title_format = lambda file, section_title, chap_title: f'{section_title} {int(file[:-4])} {chap_title}'


lk_forum_id = 173
lk_thread_id = 1020745

lk_title_format = lambda file, section_title, chap_title: chap_title
