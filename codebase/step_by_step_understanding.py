🧾 Enter your question (or 'exit' to quit): What is ikigai?

c40a16a3425bd53ccf8d3836e9a142c92af8fd350597c16490d11d629ce82e24


def generate_query_embedding(query_text: str) -> List[float]:
    print(f"\n🧠 Generating embedding for query: '{query_text}'")
    query_embedding = model.encode([query_text])[0] -> <class 'numpy.ndarray'> (1,384)
    query_embedding = l2_normalize(query_embedding)
    print(f"✅ Embedding dimension: {len(query_embedding)}")
    return query_embedding


Res: {'matches': [{'id': 'ikigai.pdf__chunk_10',
              'metadata': {'chunk_index': 10.0,
                           'end_char': 9000.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 8000.0,
                           'text': 'e a brother, even if you’ve never met them '
                                   'before.”\n'
                                   'It turns out that one of the secrets to '
                                   'happiness of Ogimi’s residents is feeling\n'
                                   'like part of a community. From an early '
                                   'age they practice yuimaaru, or\n'
                                   'teamwork, and so are used to helping one '
                                   'another.\n'
                                   'Nurturing friendships, eating light, '
                                   'getting enough rest, and doing regular,\n'
                                   'moderate exercise are all part of the '
                                   'equation of good health, but at the heart '
                                   'of\n'
                                   'the joie de vivre that inspires these '
                                   'centenarians to keep celebrating birthdays '
                                   'and\n'
                                   'cherishing each new day is their ikigai.\n'
                                   'The purpose of this book is to bring the '
                                   'secrets of Japan’s centenarians to you\n'
                                   'and give you the tools to find your own '
                                   'ikigai.\n'
                                   'Because those who discover their ikigai '
                                   'have everything they need for a long\n'
                                   'and joyful journey through life.\n'
                                   'Happy travels!\n'
                                   'HÉCTOR GARCÍA AND FRANCESC M\n'
                                   'IRALLES\n'
                                   'I\n'
                                   'IKIGAI\n'
                                   'The art of staying young while\n'
                                   'growing old\n'
                                   'What is your reason for being?\n'
                                   'According to the Japanese, everyone has an '
                                   'ikigai—what a French philosopher\n'
                                   'might call'},
              'score': 0.568400383,
              'values': []},
             {'id': 'ikigai.pdf__chunk_4',
              'metadata': {'chunk_index': 4.0,
                           'end_char': 4200.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 3200.0,
                           'text': 'igai: A mysterious word\n'
                                   'I. Ikigai\n'
                                   'The art of staying young while growing '
                                   'old\n'
                                   'II. Antiaging Secrets\n'
                                   'Little things that add up to a long and '
                                   'happy life\n'
                                   'III. From Logotherapy to Ikigai\n'
                                   'How to live longer and better by finding '
                                   'your purpose\n'
                                   'IV. Find Flow in Everything You Do\n'
                                   'How to turn work and free time into spaces '
                                   'for growth\n'
                                   'V. Masters of Longevity\n'
                                   'Words of wisdom from the longest-living '
                                   'people in the world\n'
                                   'VI. Lessons from Japan’s Centenarians\n'
                                   'Traditions and proverbs for happiness and '
                                   'longevity\n'
                                   'VII. The Ikigai Diet\n'
                                   'What the world’s longest-living people eat '
                                   'and drink\n'
                                   'VIII. Gentle Movements, Longer Life\n'
                                   'Exercises from the East that promote '
                                   'health and longevity\n'
                                   'IX. Resilience and Wabi-sabi\n'
                                   'How to face life’s challenges without '
                                   'letting stress and worry age you\n'
                                   'Epilogue\n'
                                   'Ikigai: The art of living\n'
                                   'Notes\n'
                                   'Suggestions for further reading\n'
                                   'About the Authors\n'
                                   'PROLOGUE\n'
                                   'Ikigai: A mysterious word\n'
                                   'THIS BOOK FIRST came into being on a rainy '
                                   'night in Tokyo, when its authors sat\n'
                                   'down together for the first'},
              'score': 0.530410767,
              'values': []},
             {'id': 'ikigai.pdf__chunk_11',
              'metadata': {'chunk_index': 11.0,
                           'end_char': 9800.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 8800.0,
                           'text': 'GARCÍA AND FRANCESC M\n'
                                   'IRALLES\n'
                                   'I\n'
                                   'IKIGAI\n'
                                   'The art of staying young while\n'
                                   'growing old\n'
                                   'What is your reason for being?\n'
                                   'According to the Japanese, everyone has an '
                                   'ikigai—what a French philosopher\n'
                                   'might call a raison d’être. Some people '
                                   'have found their ikigai, while others are\n'
                                   'still looking, though they carry it within '
                                   'them.\n'
                                   'Our ikigai is hidden deep inside each of '
                                   'us, and finding it requires a patient\n'
                                   'search. According to those born on '
                                   'Okinawa, the island with the most\n'
                                   'centenarians in the world, our ikigai is '
                                   'the reason we get up in the morning.\n'
                                   'Whatever you do, don’t retire!\n'
                                   'Having a clearly defined ikigai brings '
                                   'satisfaction, happiness, and meaning to '
                                   'our\n'
                                   'lives. The purpose of this book is to help '
                                   'you find yours, and to share insights\n'
                                   'from Japanese philosophy on the lasting '
                                   'health of body, mind, and spirit.\n'
                                   'One surprising thing you notice, living in '
                                   'Japan, is how active people remain\n'
                                   'after they retire. In fact, many Japanese '
                                   'people never really retire—they keep\n'
                                   'doing what they love for as'},
              'score': 0.527626038,
              'values': []},
             {'id': 'ikigai.pdf__chunk_9',
              'metadata': {'chunk_index': 9.0,
                           'end_char': 8200.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 7200.0,
                           'text': 'liness of its residents,\n'
                                   'who laughed and joked incessantly amid '
                                   'lush green hills fed by crystalline '
                                   'waters.\n'
                                   'As we conducted our interviews with the '
                                   'eldest residents of the town, we\n'
                                   'realized that something far more powerful '
                                   'than just these natural resources was at\n'
                                   'work: an uncommon joy flows from its '
                                   'inhabitants and guides them through the\n'
                                   'long and pleasurable journey of their '
                                   'lives.\n'
                                   'Again, the mysterious ikigai.\n'
                                   'But what is it, exactly? How do you get '
                                   'it?\n'
                                   'It never ceased to surprise us that this '
                                   'haven of nearly eternal life was located\n'
                                   'precisely in Okinawa, where two hundred '
                                   'thousand innocent lives were lost at the\n'
                                   'end of World War II. Rather than harbor '
                                   'animosity toward outsiders, however,\n'
                                   'Okinawans live by the principle of '
                                   'ichariba chode, a local expression that '
                                   'means\n'
                                   '“treat everyone like a brother, even if '
                                   'you’ve never met them before.”\n'
                                   'It turns out that one of the secrets to '
                                   'happiness of Ogimi’s residents is feeling\n'
                                   'like part of a community. From an early '
                                   'age they practice yuimaaru'},
              'score': 0.524535239,
              'values': []},
             {'id': 'ikigai.pdf__chunk_14',
              'metadata': {'chunk_index': 14.0,
                           'end_char': 12200.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 11200.0,
                           'text': 'sexual hormones until much later\n'
                                   'in life.\n'
                                   'The rate of dementia is well below the '
                                   'global average.\n'
                                   'The Characters Behind Ikigai\n'
                                   'In Japanese, ikigai is written as 生き甲斐, '
                                   'combining 生き, which means\n'
                                   '“life,” with 甲斐, which means “to be '
                                   'worthwhile.” 甲斐 can be broken\n'
                                   'down into the characters 甲, which means '
                                   '“armor,” “number one,” and “to\n'
                                   'be the first” (to head into battle, taking '
                                   'initiative as a leader), and 斐,\n'
                                   'which means “beautiful” or “elegant.”\n'
                                   'Though we will consider each of these '
                                   'findings over the course of the book,\n'
                                   'research clearly indicates that the '
                                   'Okinawans’ focus on ikigai gives a sense '
                                   'of\n'
                                   'purpose to each and every day and plays an '
                                   'important role in their health and\n'
                                   'longevity.\n'
                                   'The five Blue Zones\n'
                                   'Okinawa holds first place among the '
                                   'world’s Blue Zones. In Okinawa, women in\n'
                                   'particular live longer and have fewer '
                                   'diseases than anywhere else in the world.\n'
                                   'The five regions identified and analyzed '
                                   'by Dan Buettner in his book The Blue\n'
                                   'Zones are:\n'
                                   '1. Okinawa, Japan (especially the northern '
                                   'par'},
              'score': 0.482807666,
              'values': []},
             {'id': 'ikigai.pdf__chunk_221',
              'metadata': {'chunk_index': 221.0,
                           'end_char': 177800.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 176800.0,
                           'text': 'e, also by Aida, means “Keep going; don’t '
                                   'change your path.”\n'
                                   'This last one, also by Aida, means “Keep '
                                   'going; don’t change your path.”\n'
                                   'そのままでいいがな\n'
                                   'Once you discover your ikigai, pursuing it '
                                   'and nurturing it every day will bring\n'
                                   'meaning to your life. The moment your life '
                                   'has this purpose, you will achieve a\n'
                                   'happy state of flow in all you do, like '
                                   'the calligrapher at his canvas or the '
                                   'chef\n'
                                   'who, after half a century, still prepares '
                                   'sushi for his patrons with love.\n'
                                   'Conclusion\n'
                                   'Our ikigai is different for all of us, but '
                                   'one thing we have in common is that we\n'
                                   'are all searching for meaning. When we '
                                   'spend our days feeling connected to what\n'
                                   'is meaningful to us, we live more fully; '
                                   'when we lose the connection, we feel\n'
                                   'despair.\n'
                                   'Modern life estranges us more and more '
                                   'from our true nature, making it very\n'
                                   'easy for us to lead lives lacking in '
                                   'meaning. Powerful forces and incentives\n'
                                   '(money, power, attention, success) '
                                   'distract us on a daily basis; don’t let '
                                   'them take\n'
                                   'over your life.\n'
                                   'Our intuition and curio'},
              'score': 0.457759857,
              'values': []},
             {'id': 'ikigai.pdf__chunk_197',
              'metadata': {'chunk_index': 197.0,
                           'end_char': 158600.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 157600.0,
                           'text': 'keaway is that they all combine a '
                                   'physical\n'
                                   'exercise with an awareness of our breath. '
                                   'These two components—movement\n'
                                   'and breath—help us to bring our '
                                   'consciousness in line with our body, '
                                   'instead of\n'
                                   'allowing our mind to be carried away by '
                                   'the sea of daily worries. Most of the\n'
                                   'time, we are just not aware enough of our '
                                   'breathing.\n'
                                   'IX\n'
                                   'RESILIENCE AND WABI-SABI\n'
                                   'How to face life’s challenges\n'
                                   'without letting stress and worry age\n'
                                   'you\n'
                                   'What is resilience?\n'
                                   'One thing that everyone with a clearly '
                                   'defined ikigai has in common is that they\n'
                                   'pursue their passion no matter what. They '
                                   'never give up, even when the cards\n'
                                   'seem stacked against them or they face one '
                                   'hurdle after another.\n'
                                   'We’re talking about resilience, a concept '
                                   'that has become influential among\n'
                                   'psychologists.\n'
                                   'But resilience isn’t just the ability to '
                                   'persevere. As we’ll see in this chapter, '
                                   'it\n'
                                   'is also an outlook we can cultivate to '
                                   'stay focused on the important things in '
                                   'life\n'
                                   'rather than what is most urgent, and to '
                                   'keep ourselves from being carrie'},
              'score': 0.443742752,
              'values': []},
             {'id': 'ikigai.pdf__chunk_220',
              'metadata': {'chunk_index': 220.0,
                           'end_char': 177000.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 176000.0,
                           'text': 'igraphers and haikuists of the\n'
                                   'twentieth century. He is yet another '
                                   'example of a Japanese person who '
                                   'dedicated\n'
                                   'his life to a very specific ikigai: '
                                   'communicating emotions with '
                                   'seventeen-syllable\n'
                                   'poems, using a shodo calligraphy brush.\n'
                                   'Many of Aida’s haikus philosophize about '
                                   'the importance of the present\n'
                                   'moment, and the passage of time. The poem '
                                   'reproduced below could be\n'
                                   'translated as “In the here and now, the '
                                   'only thing in my life is your life.”\n'
                                   'いまここにしかないわたし\n'
                                   'のいのちあなたのいのち\n'
                                   'In another poem, Aida writes simply, '
                                   '“Here, now.” It is an artwork that seeks\n'
                                   'to evoke feelings of mono no aware (a '
                                   'melancholy appreciation of the\n'
                                   'ephemeral).\n'
                                   'いまここ\n'
                                   'The following poem touches on one of the '
                                   'secrets of bringing ikigai into our\n'
                                   'lives: “Happiness is always determined by '
                                   'your heart.”\n'
                                   'しあわせはいつも自分の心がきめる\n'
                                   'This last one, also by Aida, means “Keep '
                                   'going; don’t change your path.”\n'
                                   'This last one, also by Aida, means “Keep '
                                   'going; don’t change your path.”\n'
                                   'そのままでいいがな\n'
                                   'Once you discover your ikigai, pursuing it '
                                   'and nurturing'},
              'score': 0.44162178,
              'values': []},
             {'id': 'ikigai.pdf__chunk_6',
              'metadata': {'chunk_index': 6.0,
                           'end_char': 5800.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 4800.0,
                           'text': 'cticing therapists, who favored other '
                                   'schools of psychology, though people\n'
                                   'still search for meaning in what they do '
                                   'and how they live. We ask ourselves\n'
                                   'things like:\n'
                                   'What is the meaning of my life?\n'
                                   'Is the point just to live longer, or '
                                   'should I seek a higher purpose?\n'
                                   'Why do some people know what they want and '
                                   'have a passion for life, while\n'
                                   'others languish in confusion?\n'
                                   'At some point in our conversation, the '
                                   'mysterious word ikigai came up.\n'
                                   'This Japanese concept, which translates '
                                   'roughly as “the happiness of always\n'
                                   'being busy,” is like logotherapy, but it '
                                   'goes a step beyond. It also seems to be '
                                   'one\n'
                                   'way of explaining the extraordinary '
                                   'longevity of the Japanese, especially on '
                                   'the\n'
                                   'island of Okinawa, where there are 24.55 '
                                   'people over the age of 100 for every\n'
                                   '100,000 inhabitants—far more than the '
                                   'global average.\n'
                                   'Those who study why the inhabitants of '
                                   'this island in the south of Japan live\n'
                                   'longer than people anywhere else in the '
                                   'world believe that one of the keys—in\n'
                                   'addition to a healthful diet,'},
              'score': 0.438530922,
              'values': []},
             {'id': 'ikigai.pdf__chunk_219',
              'metadata': {'chunk_index': 219.0,
                           'end_char': 176200.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 175200.0,
                           'text': 'hit or two can be viewed as either a '
                                   'misfortune or an experience that\n'
                                   'we can apply to all areas of our lives, as '
                                   'we continually make corrections and set\n'
                                   'new and better goals. As Taleb writes in '
                                   'Antifragile, “We need randomness, mess,\n'
                                   'adventures, uncertainty, self-discovery, '
                                   'hear traumatic episodes, all these things\n'
                                   'that make life worth living.” We encourage '
                                   'those interested in the concept of\n'
                                   'antifragility to read Nassim Nicholas '
                                   'Taleb’s Antifragile.\n'
                                   'Life is pure imperfection, as the '
                                   'philosophy of wabi-sabi teaches us, and '
                                   'the\n'
                                   'passage of time shows us that everything '
                                   'is fleeting, but if you have a clear '
                                   'sense\n'
                                   'of your ikigai, each moment will hold so '
                                   'many possibilities that it will seem\n'
                                   'almost like an eternity.\n'
                                   'EPILOGUE\n'
                                   'Ikigai: The art of living\n'
                                   'Mitsuo Aida was one of the most important '
                                   'calligraphers and haikuists of the\n'
                                   'twentieth century. He is yet another '
                                   'example of a Japanese person who '
                                   'dedicated\n'
                                   'his life to a very specific ikigai: '
                                   'communicating emotions with '
                                   'seventeen-syllable\n'
                                   'poems,'},
              'score': 0.43230629,
              'values': []},
             {'id': 'ikigai.pdf__chunk_222',
              'metadata': {'chunk_index': 222.0,
                           'end_char': 178600.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 177600.0,
                           'text': 'asy for us to lead lives lacking in '
                                   'meaning. Powerful forces and incentives\n'
                                   '(money, power, attention, success) '
                                   'distract us on a daily basis; don’t let '
                                   'them take\n'
                                   'over your life.\n'
                                   'Our intuition and curiosity are very '
                                   'powerful internal compasses to help us\n'
                                   'connect with our ikigai. Follow those '
                                   'things you enjoy, and get away from or\n'
                                   'change those you dislike. Be led by your '
                                   'curiosity, and keep busy by doing things\n'
                                   'that fill you with meaning and happiness. '
                                   'It doesn’t need to be a big thing: we\n'
                                   'might find meaning in being good parents '
                                   'or in helping our neighbors.\n'
                                   'There is no perfect strategy to connecting '
                                   'with our ikigai. But what we learned\n'
                                   'from the Okinawans is that we should not '
                                   'worry too much about finding it.\n'
                                   'Life is not a problem to be solved. Just '
                                   'remember to have something that\n'
                                   'keeps you busy doing what you love while '
                                   'being surrounded by the people who\n'
                                   'love you.\n'
                                   'The ten rules of ikigai\n'
                                   'We’ll conclude this journey with ten rules '
                                   'we’ve distilled from the wisdom of the\n'
                                   'long-living residen'},
              'score': 0.424901,
              'values': []},
             {'id': 'ikigai.pdf__chunk_126',
              'metadata': {'chunk_index': 126.0,
                           'end_char': 101800.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 100800.0,
                           'text': 'get to be so old.” When asked about his\n'
                                   'secret to living so long, his answer was '
                                   '“I don’t know. I just haven’t died yet.”5\n'
                                   'Ikigai artists\n'
                                   'The secret to long life, however, is not '
                                   'held by supercentenarians alone. There '
                                   'are\n'
                                   'many people of advanced age who, though '
                                   'they haven’t made it into Guinness\n'
                                   'World Records, offer us inspiration and '
                                   'ideas for bringing energy and meaning to\n'
                                   'our lives.\n'
                                   'Artists, for example, who carry the torch '
                                   'of their ikigai instead of retiring,\n'
                                   'have this power.\n'
                                   'Art, in all its forms, is an ikigai that '
                                   'can bring happiness and purpose to our\n'
                                   'days. Enjoying or creating beauty is free, '
                                   'and something all human beings have\n'
                                   'access to.\n'
                                   'Hokusai, the Japanese artist who made '
                                   'woodblock prints in the ukiyo-e style\n'
                                   'and lived for 88 years, from the '
                                   'mid-eighteenth to the mid-nineteenth '
                                   'century,\n'
                                   'added this postscript to the first edition '
                                   'of his One Hundred Views of Mount\n'
                                   'Fuji:6\n'
                                   'All that I have produced before the age of '
                                   '70 is not worth being counted. It is at '
                                   'the age of 73 that I\n'
                                   'ha'},
              'score': 0.42100051,
              'values': []},
             {'id': 'ikigai.pdf__chunk_7',
              'metadata': {'chunk_index': 7.0,
                           'end_char': 6600.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 5600.0,
                           'text': 'lobal average.\n'
                                   'Those who study why the inhabitants of '
                                   'this island in the south of Japan live\n'
                                   'longer than people anywhere else in the '
                                   'world believe that one of the keys—in\n'
                                   'addition to a healthful diet, a simple '
                                   'life in the outdoors, green tea, and the\n'
                                   'subtropical climate (its average '
                                   'temperature is like that of Hawaii)—is the '
                                   'ikigai\n'
                                   'that shapes their lives.\n'
                                   'While researching this concept, we '
                                   'discovered that not a single book in the\n'
                                   'fields of psychology or personal '
                                   'development is dedicated to bringing this\n'
                                   'philosophy to the West.\n'
                                   'Is ikigai the reason there are more '
                                   'centenarians in Okinawa than anywhere\n'
                                   'else? How does it inspire people to stay '
                                   'active until the very end? What is the\n'
                                   'secret to a long and happy life?\n'
                                   'As we explored the matter further, we '
                                   'discovered that one place in particular,\n'
                                   'Ogimi, a rural town on the north end of '
                                   'the island with a population of three\n'
                                   'thousand, boasts the highest life '
                                   'expectancy in the world—a fact that has '
                                   'earned\n'
                                   'it the nickname the Village of Longevity.'},
              'score': 0.416454345,
              'values': []},
             {'id': 'ikigai.pdf__chunk_13',
              'metadata': {'chunk_index': 13.0,
                           'end_char': 11400.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 10400.0,
                           'text': 'ntenarians from Okinawa and\n'
                                   'other so-called Blue Zones—the geographic '
                                   'regions where people live longest—\n'
                                   'provide a number of interesting facts '
                                   'about these extraordinary human beings:\n'
                                   'Not only do they live much longer than the '
                                   'rest of the world’s population,\n'
                                   'they also suffer from fewer chronic '
                                   'illnesses such as cancer and heart\n'
                                   'disease; inflammatory disorders are also '
                                   'less common.\n'
                                   'Many of these centenarians enjoy enviable '
                                   'levels of vitality and health that\n'
                                   'would be unthinkable for people of '
                                   'advanced age elsewhere.\n'
                                   'Their blood tests reveal fewer free '
                                   'radicals (which are responsible for\n'
                                   'cellular aging), as a result of drinking '
                                   'tea and eating until their stomachs are\n'
                                   'only 80 percent full.\n'
                                   'Women experience more moderate symptoms '
                                   'during menopause, and both\n'
                                   'men and women maintain higher levels of '
                                   'sexual hormones until much later\n'
                                   'in life.\n'
                                   'The rate of dementia is well below the '
                                   'global average.\n'
                                   'The Characters Behind Ikigai\n'
                                   'In Japanese, ikigai is written as 生き甲斐, '
                                   'combining 生き, which means\n'
                                   '“life,”'},
              'score': 0.414359123,
              'values': []},
             {'id': 'ikigai.pdf__chunk_3',
              'metadata': {'chunk_index': 3.0,
                           'end_char': 3400.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 2400.0,
                           'text': 'addresses, and other contact information '
                                   'at the\n'
                                   'time of publication, neither the publisher '
                                   'nor the author assumes any responsibility '
                                   'for errors or for changes that occur after '
                                   'publication.\n'
                                   'Further, the publisher does not have any '
                                   'control over and does not assume any '
                                   'responsibility for author or third-party '
                                   'Web sites or their\n'
                                   'content.\n'
                                   'Cover illustration by Olga Grlic\n'
                                   'Cover art direction by Roseanne Serra\n'
                                   'Version_2\n'
                                   'For my brother, Aitor,\n'
                                   'who’s said to me more often than anyone '
                                   'else,\n'
                                   '“I don’t know what to do with my life.”\n'
                                   '—HÉCTOR GARCÍA\n'
                                   'For all my past, present, and future '
                                   'friends,\n'
                                   'for being my home and my motivation along\n'
                                   'the way.\n'
                                   '—FRANCESC MIRALLES\n'
                                   'Only staying active will make you want to '
                                   'live a hundred years.\n'
                                   '—Japanese proverb\n'
                                   'CONTENTS\n'
                                   'Title Page\n'
                                   'Copyright\n'
                                   'Dedication\n'
                                   'Epigraph\n'
                                   'Prologue\n'
                                   'Ikigai: A mysterious word\n'
                                   'I. Ikigai\n'
                                   'The art of staying young while growing '
                                   'old\n'
                                   'II. Antiaging Secrets\n'
                                   'Little things that add up to a long and '
                                   'happy life\n'
                                   'III. From Logotherapy to Ikigai\n'
                                   'How to live longer'},
              'score': 0.397349358,
              'values': []},
             {'id': 'ikigai.pdf__chunk_65',
              'metadata': {'chunk_index': 65.0,
                           'end_char': 53000.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 52000.0,
                           'text': 's on\n'
                                   'three questions the individual must ask '
                                   'him-or herself:\n'
                                   '1. What have I received from person X?\n'
                                   '2. What have I given to person X?\n'
                                   '3. What problems have I caused person X?\n'
                                   'Through these reflections, we stop '
                                   'identifying others as the cause of our\n'
                                   'problems and deepen our own sense of '
                                   'responsibility. As Morita said, “If you '
                                   'are\n'
                                   'angry and want to fight, think about it '
                                   'for three days before coming to blows.\n'
                                   'After three days, the intense desire to '
                                   'fight will pass on its own.”7\n'
                                   'And now, ikigai\n'
                                   'Logotherapy and Morita therapy are both '
                                   'grounded in a personal, unique\n'
                                   'experience that you can access without '
                                   'therapists or spiritual retreats: the '
                                   'mission\n'
                                   'of finding your ikigai, your existential '
                                   'fuel. Once you find it, it is only a '
                                   'matter of\n'
                                   'having the courage and making the effort '
                                   'to stay on the right path.\n'
                                   'In the following chapters, we’ll take a '
                                   'look at the basic tools you’ll need to '
                                   'get\n'
                                   'moving along that path: finding flow in '
                                   'the tasks you’ve chosen to do, eating in '
                                   'a\n'
                                   'balanced and mindful way, d'},
              'score': 0.38858512,
              'values': []},
             {'id': 'ikigai.pdf__chunk_21',
              'metadata': {'chunk_index': 21.0,
                           'end_char': 17800.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 16800.0,
                           'text': 'o the group. This\n'
                                   'payment allows them to participate in '
                                   'meetings, dinners, games of go and shogi\n'
                                   '(Japanese chess), or whatever hobby they '
                                   'have in common.\n'
                                   'The funds collected by the group are used '
                                   'for activities, but if there is money\n'
                                   'left over, one member (decided on a '
                                   'rotating basis) receives a set amount '
                                   'from\n'
                                   'the surplus. In this way, being part of a '
                                   'moai helps maintain emotional and\n'
                                   'financial stability. If a member of a moai '
                                   'is in financial trouble, he or she can '
                                   'get\n'
                                   'an advance from the group’s savings. While '
                                   'the details of each moai’s accounting\n'
                                   'practices vary according to the group and '
                                   'its economic means, the feeling of\n'
                                   'belonging and support gives the individual '
                                   'a sense of security and helps increase\n'
                                   'life expectancy.\n'
                                   '• • •\n'
                                   'FOLLOWING THIS BRIEF introduction to the '
                                   'topics covered in this book, we look at\n'
                                   'a few causes of premature aging in modern '
                                   'life, and then explore different\n'
                                   'factors related to ikigai.\n'
                                   'II\n'
                                   'ANTIAGING SECRETS\n'
                                   'Little things that add up to a long\n'
                                   'and happy life\n'
                                   'Aging’s'},
              'score': 0.388457298,
              'values': []},
             {'id': 'ikigai.pdf__chunk_17',
              'metadata': {'chunk_index': 17.0,
                           'end_char': 14600.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 13600.0,
                           'text': 'it is worth\n'
                                   'pointing out that three of these regions '
                                   'are islands, where resources can be '
                                   'scarce\n'
                                   'and communities have to help one another.\n'
                                   'For many, helping others might be an '
                                   'ikigai strong enough to keep them alive.\n'
                                   'According to scientists who have studied '
                                   'the five Blue Zones, the keys to\n'
                                   'longevity are diet, exercise, finding a '
                                   'purpose in life (an ikigai), and forming\n'
                                   'strong social ties—that is, having a broad '
                                   'circle of friends and good family\n'
                                   'relations.\n'
                                   'Members of these communities manage their '
                                   'time well in order to reduce\n'
                                   'stress, consume little meat or processed '
                                   'foods, and drink alcohol in moderation.1\n'
                                   'They don’t do strenuous exercise, but they '
                                   'do move every day, taking walks\n'
                                   'and working in their vegetable gardens. '
                                   'People in the Blue Zones would rather\n'
                                   'walk than drive. Gardening, which involves '
                                   'daily low-intensity movement, is a\n'
                                   'practice almost all of them have in '
                                   'common.\n'
                                   'The 80 percent secret\n'
                                   'One of the most common sayings in Japan is '
                                   '“Hara hachi bu,” which is repeated\n'
                                   'before or aft'},
              'score': 0.364305973,
              'values': []},
             {'id': 'ikigai.pdf__chunk_1',
              'metadata': {'chunk_index': 1.0,
                           'end_char': 1800.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 800.0,
                           'text': 'All other illustrations copyright © 2016 '
                                   'by Marisa Martínez Graphics copyright © '
                                   '2016 by Flora\n'
                                   'Buki\n'
                                   'LIBRARY OF CONGRESS '
                                   'CATALOGING-IN-PUBLICATION DATA Names: '
                                   'García, Héctor, 1981– author. | Miralles, '
                                   'Francesc, 1968– author.\n'
                                   'Title: Ikigai : the Japanese secret to a '
                                   'long and happy life / Héctor García and '
                                   'Francesc Miralles ; translated by Heather '
                                   'Cleary.\n'
                                   'Other titles: Ikigai. English\n'
                                   'Description: New York : Penguin Books, '
                                   '[2017] | Originally published in Spanish '
                                   'as “Ikigai: Los secretos de Japón para una '
                                   'vida larga y\n'
                                   'feliz” by Ediciones Urano in 2016." | '
                                   'Includes bibliographical references. | '
                                   'Description based on print version record '
                                   'and CIP data\n'
                                   'provided by publisher; resource not '
                                   'viewed.\n'
                                   'Identifiers: LCCN 2017005811 (print) | '
                                   'LCCN 2017022599 (ebook) | ISBN '
                                   '9781524704551 (ebook) | ISBN '
                                   '9780143130727\n'
                                   '(hardcover) Subjects: LCSH: '
                                   'Longevity—Japan. | Longevity. | Happiness. '
                                   '| Quality of life Classification: LCC '
                                   'RA776.75 (ebook) | LCC\n'
                                   'RA776.75 .G3713 2017 (print) | DDC '
                                   '613—dc23\n'
                                   'LC record ava'},
              'score': 0.356697083,
              'values': []},
             {'id': 'ikigai.pdf__chunk_154',
              'metadata': {'chunk_index': 154.0,
                           'end_char': 124200.0,
                           'namespace': 'my_corpus',
                           'source': 'ikigai.pdf',
                           'start_char': 123200.0,
                           'text': 'ential parts of daily life.\n'
                                   'They have an important purpose in life, or '
                                   'several. They have an ikigai,\n'
                                   'but they don’t take it too seriously. They '
                                   'are relaxed and enjoy all that\n'
                                   'they do.\n'
                                   'They are very proud of their traditions '
                                   'and local culture.\n'
                                   'They are passionate about everything they '
                                   'do, however insignificant it\n'
                                   'might seem.\n'
                                   'Locals have a strong sense of '
                                   'yuimaaru—recognizing the connection\n'
                                   'between people. They help each other with '
                                   'everything from work in the\n'
                                   'fields (harvesting sugarcane or planting '
                                   'rice) to building houses and\n'
                                   'municipal projects. Our friend Miyagi, who '
                                   'ate dinner with us on our\n'
                                   'last night in town, told us that he was '
                                   'building a new home with the help\n'
                                   'of all his friends, and that we could stay '
                                   'there the next time we were in\n'
                                   'Ogimi.\n'
                                   'They are always busy, but they occupy '
                                   'themselves with tasks that allow\n'
                                   'them to relax. We didn’t see a single old '
                                   'grandpa sitting on a bench\n'
                                   'doing nothing. They’re always coming and '
                                   'going—to sing karaoke, visit\n'
                                   'with neighbors, or play a game of'},
              'score': 0.354898453,
              'values': []}],
 'namespace': 'my_corpus',
 'usage': {'read_units': 1}}

candidate_ids: ['ikigai.pdf__chunk_10', 'ikigai.pdf__chunk_4', 'ikigai.pdf__chunk_11', 'ikigai.pdf__chunk_9', 'ikigai.pdf__chunk_14', 'ikigai.pdf__chunk_221', 'ikigai.pdf__chunk_197', 'ikigai.pdf__chunk_220', 'ikigai.pdf__chunk_6', 'ikigai.pdf__chunk_219', 'ikigai.pdf__chunk_222', 'ikigai.pdf__chunk_126', 'ikigai.pdf__chunk_7', 'ikigai.pdf__chunk_13', 'ikigai.pdf__chunk_3', 'ikigai.pdf__chunk_65', 'ikigai.pdf__chunk_21', 'ikigai.pdf__chunk_17', 'ikigai.pdf__chunk_1', 'ikigai.pdf__chunk_154']


candidate_texts: ['e a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru, or\nteamwork, and so are used to helping one another.\nNurturing friendships, eating light, getting enough rest, and doing regular,\nmoderate exercise are all part of the equation of good health, but at the heart of\nthe joie de vivre that inspires these centenarians to keep celebrating birthdays and\ncherishing each new day is their ikigai.\nThe purpose of this book is to bring the secrets of Japan’s centenarians to you\nand give you the tools to find your own ikigai.\nBecause those who discover their ikigai have everything they need for a long\nand joyful journey through life.\nHappy travels!\nHÉCTOR GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call', 'igai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer and better by finding your purpose\nIV. Find Flow in Everything You Do\nHow to turn work and free time into spaces for growth\nV. Masters of Longevity\nWords of wisdom from the longest-living people in the world\nVI. Lessons from Japan’s Centenarians\nTraditions and proverbs for happiness and longevity\nVII. The Ikigai Diet\nWhat the world’s longest-living people eat and drink\nVIII. Gentle Movements, Longer Life\nExercises from the East that promote health and longevity\nIX. Resilience and Wabi-sabi\nHow to face life’s challenges without letting stress and worry age you\nEpilogue\nIkigai: The art of living\nNotes\nSuggestions for further reading\nAbout the Authors\nPROLOGUE\nIkigai: A mysterious word\nTHIS BOOK FIRST came into being on a rainy night in Tokyo, when its authors sat\ndown together for the first', 'GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call a raison d’être. Some people have found their ikigai, while others are\nstill looking, though they carry it within them.\nOur ikigai is hidden deep inside each of us, and finding it requires a patient\nsearch. According to those born on Okinawa, the island with the most\ncentenarians in the world, our ikigai is the reason we get up in the morning.\nWhatever you do, don’t retire!\nHaving a clearly defined ikigai brings satisfaction, happiness, and meaning to our\nlives. The purpose of this book is to help you find yours, and to share insights\nfrom Japanese philosophy on the lasting health of body, mind, and spirit.\nOne surprising thing you notice, living in Japan, is how active people remain\nafter they retire. In fact, many Japanese people never really retire—they keep\ndoing what they love for as', 'liness of its residents,\nwho laughed and joked incessantly amid lush green hills fed by crystalline waters.\nAs we conducted our interviews with the eldest residents of the town, we\nrealized that something far more powerful than just these natural resources was at\nwork: an uncommon joy flows from its inhabitants and guides them through the\nlong and pleasurable journey of their lives.\nAgain, the mysterious ikigai.\nBut what is it, exactly? How do you get it?\nIt never ceased to surprise us that this haven of nearly eternal life was located\nprecisely in Okinawa, where two hundred thousand innocent lives were lost at the\nend of World War II. Rather than harbor animosity toward outsiders, however,\nOkinawans live by the principle of ichariba chode, a local expression that means\n“treat everyone like a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru', 'sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,” with 甲斐, which means “to be worthwhile.” 甲斐 can be broken\ndown into the characters 甲, which means “armor,” “number one,” and “to\nbe the first” (to head into battle, taking initiative as a leader), and 斐,\nwhich means “beautiful” or “elegant.”\nThough we will consider each of these findings over the course of the book,\nresearch clearly indicates that the Okinawans’ focus on ikigai gives a sense of\npurpose to each and every day and plays an important role in their health and\nlongevity.\nThe five Blue Zones\nOkinawa holds first place among the world’s Blue Zones. In Okinawa, women in\nparticular live longer and have fewer diseases than anywhere else in the world.\nThe five regions identified and analyzed by Dan Buettner in his book The Blue\nZones are:\n1. Okinawa, Japan (especially the northern par', 'e, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing it every day will bring\nmeaning to your life. The moment your life has this purpose, you will achieve a\nhappy state of flow in all you do, like the calligrapher at his canvas or the chef\nwho, after half a century, still prepares sushi for his patrons with love.\nConclusion\nOur ikigai is different for all of us, but one thing we have in common is that we\nare all searching for meaning. When we spend our days feeling connected to what\nis meaningful to us, we live more fully; when we lose the connection, we feel\ndespair.\nModern life estranges us more and more from our true nature, making it very\neasy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curio', 'keaway is that they all combine a physical\nexercise with an awareness of our breath. These two components—movement\nand breath—help us to bring our consciousness in line with our body, instead of\nallowing our mind to be carried away by the sea of daily worries. Most of the\ntime, we are just not aware enough of our breathing.\nIX\nRESILIENCE AND WABI-SABI\nHow to face life’s challenges\nwithout letting stress and worry age\nyou\nWhat is resilience?\nOne thing that everyone with a clearly defined ikigai has in common is that they\npursue their passion no matter what. They never give up, even when the cards\nseem stacked against them or they face one hurdle after another.\nWe’re talking about resilience, a concept that has become influential among\npsychologists.\nBut resilience isn’t just the ability to persevere. As we’ll see in this chapter, it\nis also an outlook we can cultivate to stay focused on the important things in life\nrather than what is most urgent, and to keep ourselves from being carrie', 'igraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems, using a shodo calligraphy brush.\nMany of Aida’s haikus philosophize about the importance of the present\nmoment, and the passage of time. The poem reproduced below could be\ntranslated as “In the here and now, the only thing in my life is your life.”\nいまここにしかないわたし\nのいのちあなたのいのち\nIn another poem, Aida writes simply, “Here, now.” It is an artwork that seeks\nto evoke feelings of mono no aware (a melancholy appreciation of the\nephemeral).\nいまここ\nThe following poem touches on one of the secrets of bringing ikigai into our\nlives: “Happiness is always determined by your heart.”\nしあわせはいつも自分の心がきめる\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing', 'cticing therapists, who favored other schools of psychology, though people\nstill search for meaning in what they do and how they live. We ask ourselves\nthings like:\nWhat is the meaning of my life?\nIs the point just to live longer, or should I seek a higher purpose?\nWhy do some people know what they want and have a passion for life, while\nothers languish in confusion?\nAt some point in our conversation, the mysterious word ikigai came up.\nThis Japanese concept, which translates roughly as “the happiness of always\nbeing busy,” is like logotherapy, but it goes a step beyond. It also seems to be one\nway of explaining the extraordinary longevity of the Japanese, especially on the\nisland of Okinawa, where there are 24.55 people over the age of 100 for every\n100,000 inhabitants—far more than the global average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet,', 'hit or two can be viewed as either a misfortune or an experience that\nwe can apply to all areas of our lives, as we continually make corrections and set\nnew and better goals. As Taleb writes in Antifragile, “We need randomness, mess,\nadventures, uncertainty, self-discovery, hear traumatic episodes, all these things\nthat make life worth living.” We encourage those interested in the concept of\nantifragility to read Nassim Nicholas Taleb’s Antifragile.\nLife is pure imperfection, as the philosophy of wabi-sabi teaches us, and the\npassage of time shows us that everything is fleeting, but if you have a clear sense\nof your ikigai, each moment will hold so many possibilities that it will seem\nalmost like an eternity.\nEPILOGUE\nIkigai: The art of living\nMitsuo Aida was one of the most important calligraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems,', 'asy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curiosity are very powerful internal compasses to help us\nconnect with our ikigai. Follow those things you enjoy, and get away from or\nchange those you dislike. Be led by your curiosity, and keep busy by doing things\nthat fill you with meaning and happiness. It doesn’t need to be a big thing: we\nmight find meaning in being good parents or in helping our neighbors.\nThere is no perfect strategy to connecting with our ikigai. But what we learned\nfrom the Okinawans is that we should not worry too much about finding it.\nLife is not a problem to be solved. Just remember to have something that\nkeeps you busy doing what you love while being surrounded by the people who\nlove you.\nThe ten rules of ikigai\nWe’ll conclude this journey with ten rules we’ve distilled from the wisdom of the\nlong-living residen', 'get to be so old.” When asked about his\nsecret to living so long, his answer was “I don’t know. I just haven’t died yet.”5\nIkigai artists\nThe secret to long life, however, is not held by supercentenarians alone. There are\nmany people of advanced age who, though they haven’t made it into Guinness\nWorld Records, offer us inspiration and ideas for bringing energy and meaning to\nour lives.\nArtists, for example, who carry the torch of their ikigai instead of retiring,\nhave this power.\nArt, in all its forms, is an ikigai that can bring happiness and purpose to our\ndays. Enjoying or creating beauty is free, and something all human beings have\naccess to.\nHokusai, the Japanese artist who made woodblock prints in the ukiyo-e style\nand lived for 88 years, from the mid-eighteenth to the mid-nineteenth century,\nadded this postscript to the first edition of his One Hundred Views of Mount\nFuji:6\nAll that I have produced before the age of 70 is not worth being counted. It is at the age of 73 that I\nha', 'lobal average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet, a simple life in the outdoors, green tea, and the\nsubtropical climate (its average temperature is like that of Hawaii)—is the ikigai\nthat shapes their lives.\nWhile researching this concept, we discovered that not a single book in the\nfields of psychology or personal development is dedicated to bringing this\nphilosophy to the West.\nIs ikigai the reason there are more centenarians in Okinawa than anywhere\nelse? How does it inspire people to stay active until the very end? What is the\nsecret to a long and happy life?\nAs we explored the matter further, we discovered that one place in particular,\nOgimi, a rural town on the north end of the island with a population of three\nthousand, boasts the highest life expectancy in the world—a fact that has earned\nit the nickname the Village of Longevity.', 'ntenarians from Okinawa and\nother so-called Blue Zones—the geographic regions where people live longest—\nprovide a number of interesting facts about these extraordinary human beings:\nNot only do they live much longer than the rest of the world’s population,\nthey also suffer from fewer chronic illnesses such as cancer and heart\ndisease; inflammatory disorders are also less common.\nMany of these centenarians enjoy enviable levels of vitality and health that\nwould be unthinkable for people of advanced age elsewhere.\nTheir blood tests reveal fewer free radicals (which are responsible for\ncellular aging), as a result of drinking tea and eating until their stomachs are\nonly 80 percent full.\nWomen experience more moderate symptoms during menopause, and both\nmen and women maintain higher levels of sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,”', 'addresses, and other contact information at the\ntime of publication, neither the publisher nor the author assumes any responsibility for errors or for changes that occur after publication.\nFurther, the publisher does not have any control over and does not assume any responsibility for author or third-party Web sites or their\ncontent.\nCover illustration by Olga Grlic\nCover art direction by Roseanne Serra\nVersion_2\nFor my brother, Aitor,\nwho’s said to me more often than anyone else,\n“I don’t know what to do with my life.”\n—HÉCTOR GARCÍA\nFor all my past, present, and future friends,\nfor being my home and my motivation along\nthe way.\n—FRANCESC MIRALLES\nOnly staying active will make you want to live a hundred years.\n—Japanese proverb\nCONTENTS\nTitle Page\nCopyright\nDedication\nEpigraph\nPrologue\nIkigai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer', 's on\nthree questions the individual must ask him-or herself:\n1. What have I received from person X?\n2. What have I given to person X?\n3. What problems have I caused person X?\nThrough these reflections, we stop identifying others as the cause of our\nproblems and deepen our own sense of responsibility. As Morita said, “If you are\nangry and want to fight, think about it for three days before coming to blows.\nAfter three days, the intense desire to fight will pass on its own.”7\nAnd now, ikigai\nLogotherapy and Morita therapy are both grounded in a personal, unique\nexperience that you can access without therapists or spiritual retreats: the mission\nof finding your ikigai, your existential fuel. Once you find it, it is only a matter of\nhaving the courage and making the effort to stay on the right path.\nIn the following chapters, we’ll take a look at the basic tools you’ll need to get\nmoving along that path: finding flow in the tasks you’ve chosen to do, eating in a\nbalanced and mindful way, d', 'o the group. This\npayment allows them to participate in meetings, dinners, games of go and shogi\n(Japanese chess), or whatever hobby they have in common.\nThe funds collected by the group are used for activities, but if there is money\nleft over, one member (decided on a rotating basis) receives a set amount from\nthe surplus. In this way, being part of a moai helps maintain emotional and\nfinancial stability. If a member of a moai is in financial trouble, he or she can get\nan advance from the group’s savings. While the details of each moai’s accounting\npractices vary according to the group and its economic means, the feeling of\nbelonging and support gives the individual a sense of security and helps increase\nlife expectancy.\n• • •\nFOLLOWING THIS BRIEF introduction to the topics covered in this book, we look at\na few causes of premature aging in modern life, and then explore different\nfactors related to ikigai.\nII\nANTIAGING SECRETS\nLittle things that add up to a long\nand happy life\nAging’s', 'it is worth\npointing out that three of these regions are islands, where resources can be scarce\nand communities have to help one another.\nFor many, helping others might be an ikigai strong enough to keep them alive.\nAccording to scientists who have studied the five Blue Zones, the keys to\nlongevity are diet, exercise, finding a purpose in life (an ikigai), and forming\nstrong social ties—that is, having a broad circle of friends and good family\nrelations.\nMembers of these communities manage their time well in order to reduce\nstress, consume little meat or processed foods, and drink alcohol in moderation.1\nThey don’t do strenuous exercise, but they do move every day, taking walks\nand working in their vegetable gardens. People in the Blue Zones would rather\nwalk than drive. Gardening, which involves daily low-intensity movement, is a\npractice almost all of them have in common.\nThe 80 percent secret\nOne of the most common sayings in Japan is “Hara hachi bu,” which is repeated\nbefore or aft', 'All other illustrations copyright © 2016 by Marisa Martínez Graphics copyright © 2016 by Flora\nBuki\nLIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Names: García, Héctor, 1981– author. | Miralles, Francesc, 1968– author.\nTitle: Ikigai : the Japanese secret to a long and happy life / Héctor García and Francesc Miralles ; translated by Heather Cleary.\nOther titles: Ikigai. English\nDescription: New York : Penguin Books, [2017] | Originally published in Spanish as “Ikigai: Los secretos de Japón para una vida larga y\nfeliz” by Ediciones Urano in 2016." | Includes bibliographical references. | Description based on print version record and CIP data\nprovided by publisher; resource not viewed.\nIdentifiers: LCCN 2017005811 (print) | LCCN 2017022599 (ebook) | ISBN 9781524704551 (ebook) | ISBN 9780143130727\n(hardcover) Subjects: LCSH: Longevity—Japan. | Longevity. | Happiness. | Quality of life Classification: LCC RA776.75 (ebook) | LCC\nRA776.75 .G3713 2017 (print) | DDC 613—dc23\nLC record ava', 'ential parts of daily life.\nThey have an important purpose in life, or several. They have an ikigai,\nbut they don’t take it too seriously. They are relaxed and enjoy all that\nthey do.\nThey are very proud of their traditions and local culture.\nThey are passionate about everything they do, however insignificant it\nmight seem.\nLocals have a strong sense of yuimaaru—recognizing the connection\nbetween people. They help each other with everything from work in the\nfields (harvesting sugarcane or planting rice) to building houses and\nmunicipal projects. Our friend Miyagi, who ate dinner with us on our\nlast night in town, told us that he was building a new home with the help\nof all his friends, and that we could stay there the next time we were in\nOgimi.\nThey are always busy, but they occupy themselves with tasks that allow\nthem to relax. We didn’t see a single old grandpa sitting on a bench\ndoing nothing. They’re always coming and going—to sing karaoke, visit\nwith neighbors, or play a game of']

vector_scores: [0.568400383, 0.530410767, 0.527626038, 0.524535239, 0.482807666, 0.457759857, 0.443742752, 0.44162178, 0.438530922, 0.43230629, 0.424901, 0.42100051, 0.416454345, 0.414359123, 0.397349358, 0.38858512, 0.388457298, 0.364305973, 0.356697083, 0.354898453]

bm25_raw: [3.2083990919176255, 3.6593976500396934, 4.19573253772926, 0.6657765329344102, 2.9848916477986225, 2.391700537313845, 2.725009211398346, 1.8306990514898425, 2.870205723344265, 0.0, 2.693301402869361, 2.9462308954035965, 3.201928439661942, 2.6281326306764807, 3.254453410269138, 2.833517299222413, 0.0, 1.8016986469438923, 1.8968517232673605, 0.0]

bm25_norm: [0.7646815098595438, 0.8721713353111321, 1.0, 0.1586794503576079, 0.7114113259025926, 0.5700316966839453, 0.649471620722785, 0.43632405903561744, 0.684077380417968, 0.0, 0.6419144639584157, 0.7021970225485592, 0.7631393114001573, 0.626382307986398, 0.7756579765283265, 0.6753331566639659, 0.0, 0.42941217790754976, 0.4520907150802184, 0.0]

hybrid_scores: [0.6174706647148859, 0.6158509090777831, 0.6457195284999999, 0.43307129183940196, 0.5399585809756482, 0.4858278169209863, 0.49517496918069626, 0.4402973497589044, 0.499917536604492, 0.32422971749999996, 0.4791543659896039, 0.4912996381371398, 0.5031255866000394, 0.4673649192465995, 0.4919265126320816, 0.4602721291659915, 0.2913429735, 0.38058252422688743, 0.38054549102005464, 0.26617383975]

candidates: [{'id': 'ikigai.pdf__chunk_10', 'text': 'e a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru, or\nteamwork, and so are used to helping one another.\nNurturing friendships, eating light, getting enough rest, and doing regular,\nmoderate exercise are all part of the equation of good health, but at the heart of\nthe joie de vivre that inspires these centenarians to keep celebrating birthdays and\ncherishing each new day is their ikigai.\nThe purpose of this book is to bring the secrets of Japan’s centenarians to you\nand give you the tools to find your own ikigai.\nBecause those who discover their ikigai have everything they need for a long\nand joyful journey through life.\nHappy travels!\nHÉCTOR GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call', 'vector_score': 0.568400383, 'hybrid_score': 0.6174706647148859}, {'id': 'ikigai.pdf__chunk_4', 'text': 'igai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer and better by finding your purpose\nIV. Find Flow in Everything You Do\nHow to turn work and free time into spaces for growth\nV. Masters of Longevity\nWords of wisdom from the longest-living people in the world\nVI. Lessons from Japan’s Centenarians\nTraditions and proverbs for happiness and longevity\nVII. The Ikigai Diet\nWhat the world’s longest-living people eat and drink\nVIII. Gentle Movements, Longer Life\nExercises from the East that promote health and longevity\nIX. Resilience and Wabi-sabi\nHow to face life’s challenges without letting stress and worry age you\nEpilogue\nIkigai: The art of living\nNotes\nSuggestions for further reading\nAbout the Authors\nPROLOGUE\nIkigai: A mysterious word\nTHIS BOOK FIRST came into being on a rainy night in Tokyo, when its authors sat\ndown together for the first', 'vector_score': 0.530410767, 'hybrid_score': 0.6158509090777831}, {'id': 'ikigai.pdf__chunk_11', 'text': 'GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call a raison d’être. Some people have found their ikigai, while others are\nstill looking, though they carry it within them.\nOur ikigai is hidden deep inside each of us, and finding it requires a patient\nsearch. According to those born on Okinawa, the island with the most\ncentenarians in the world, our ikigai is the reason we get up in the morning.\nWhatever you do, don’t retire!\nHaving a clearly defined ikigai brings satisfaction, happiness, and meaning to our\nlives. The purpose of this book is to help you find yours, and to share insights\nfrom Japanese philosophy on the lasting health of body, mind, and spirit.\nOne surprising thing you notice, living in Japan, is how active people remain\nafter they retire. In fact, many Japanese people never really retire—they keep\ndoing what they love for as', 'vector_score': 0.527626038, 'hybrid_score': 0.6457195284999999}, {'id': 'ikigai.pdf__chunk_9', 'text': 'liness of its residents,\nwho laughed and joked incessantly amid lush green hills fed by crystalline waters.\nAs we conducted our interviews with the eldest residents of the town, we\nrealized that something far more powerful than just these natural resources was at\nwork: an uncommon joy flows from its inhabitants and guides them through the\nlong and pleasurable journey of their lives.\nAgain, the mysterious ikigai.\nBut what is it, exactly? How do you get it?\nIt never ceased to surprise us that this haven of nearly eternal life was located\nprecisely in Okinawa, where two hundred thousand innocent lives were lost at the\nend of World War II. Rather than harbor animosity toward outsiders, however,\nOkinawans live by the principle of ichariba chode, a local expression that means\n“treat everyone like a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru', 'vector_score': 0.524535239, 'hybrid_score': 0.43307129183940196}, {'id': 'ikigai.pdf__chunk_14', 'text': 'sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,” with 甲斐, which means “to be worthwhile.” 甲斐 can be broken\ndown into the characters 甲, which means “armor,” “number one,” and “to\nbe the first” (to head into battle, taking initiative as a leader), and 斐,\nwhich means “beautiful” or “elegant.”\nThough we will consider each of these findings over the course of the book,\nresearch clearly indicates that the Okinawans’ focus on ikigai gives a sense of\npurpose to each and every day and plays an important role in their health and\nlongevity.\nThe five Blue Zones\nOkinawa holds first place among the world’s Blue Zones. In Okinawa, women in\nparticular live longer and have fewer diseases than anywhere else in the world.\nThe five regions identified and analyzed by Dan Buettner in his book The Blue\nZones are:\n1. Okinawa, Japan (especially the northern par', 'vector_score': 0.482807666, 'hybrid_score': 0.5399585809756482}, {'id': 'ikigai.pdf__chunk_221', 'text': 'e, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing it every day will bring\nmeaning to your life. The moment your life has this purpose, you will achieve a\nhappy state of flow in all you do, like the calligrapher at his canvas or the chef\nwho, after half a century, still prepares sushi for his patrons with love.\nConclusion\nOur ikigai is different for all of us, but one thing we have in common is that we\nare all searching for meaning. When we spend our days feeling connected to what\nis meaningful to us, we live more fully; when we lose the connection, we feel\ndespair.\nModern life estranges us more and more from our true nature, making it very\neasy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curio', 'vector_score': 0.457759857, 'hybrid_score': 0.4858278169209863}, {'id': 'ikigai.pdf__chunk_197', 'text': 'keaway is that they all combine a physical\nexercise with an awareness of our breath. These two components—movement\nand breath—help us to bring our consciousness in line with our body, instead of\nallowing our mind to be carried away by the sea of daily worries. Most of the\ntime, we are just not aware enough of our breathing.\nIX\nRESILIENCE AND WABI-SABI\nHow to face life’s challenges\nwithout letting stress and worry age\nyou\nWhat is resilience?\nOne thing that everyone with a clearly defined ikigai has in common is that they\npursue their passion no matter what. They never give up, even when the cards\nseem stacked against them or they face one hurdle after another.\nWe’re talking about resilience, a concept that has become influential among\npsychologists.\nBut resilience isn’t just the ability to persevere. As we’ll see in this chapter, it\nis also an outlook we can cultivate to stay focused on the important things in life\nrather than what is most urgent, and to keep ourselves from being carrie', 'vector_score': 0.443742752, 'hybrid_score': 0.49517496918069626}, {'id': 'ikigai.pdf__chunk_220', 'text': 'igraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems, using a shodo calligraphy brush.\nMany of Aida’s haikus philosophize about the importance of the present\nmoment, and the passage of time. The poem reproduced below could be\ntranslated as “In the here and now, the only thing in my life is your life.”\nいまここにしかないわたし\nのいのちあなたのいのち\nIn another poem, Aida writes simply, “Here, now.” It is an artwork that seeks\nto evoke feelings of mono no aware (a melancholy appreciation of the\nephemeral).\nいまここ\nThe following poem touches on one of the secrets of bringing ikigai into our\nlives: “Happiness is always determined by your heart.”\nしあわせはいつも自分の心がきめる\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing', 'vector_score': 0.44162178, 'hybrid_score': 0.4402973497589044}, {'id': 'ikigai.pdf__chunk_6', 'text': 'cticing therapists, who favored other schools of psychology, though people\nstill search for meaning in what they do and how they live. We ask ourselves\nthings like:\nWhat is the meaning of my life?\nIs the point just to live longer, or should I seek a higher purpose?\nWhy do some people know what they want and have a passion for life, while\nothers languish in confusion?\nAt some point in our conversation, the mysterious word ikigai came up.\nThis Japanese concept, which translates roughly as “the happiness of always\nbeing busy,” is like logotherapy, but it goes a step beyond. It also seems to be one\nway of explaining the extraordinary longevity of the Japanese, especially on the\nisland of Okinawa, where there are 24.55 people over the age of 100 for every\n100,000 inhabitants—far more than the global average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet,', 'vector_score': 0.438530922, 'hybrid_score': 0.499917536604492}, {'id': 'ikigai.pdf__chunk_219', 'text': 'hit or two can be viewed as either a misfortune or an experience that\nwe can apply to all areas of our lives, as we continually make corrections and set\nnew and better goals. As Taleb writes in Antifragile, “We need randomness, mess,\nadventures, uncertainty, self-discovery, hear traumatic episodes, all these things\nthat make life worth living.” We encourage those interested in the concept of\nantifragility to read Nassim Nicholas Taleb’s Antifragile.\nLife is pure imperfection, as the philosophy of wabi-sabi teaches us, and the\npassage of time shows us that everything is fleeting, but if you have a clear sense\nof your ikigai, each moment will hold so many possibilities that it will seem\nalmost like an eternity.\nEPILOGUE\nIkigai: The art of living\nMitsuo Aida was one of the most important calligraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems,', 'vector_score': 0.43230629, 'hybrid_score': 0.32422971749999996}, {'id': 'ikigai.pdf__chunk_222', 'text': 'asy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curiosity are very powerful internal compasses to help us\nconnect with our ikigai. Follow those things you enjoy, and get away from or\nchange those you dislike. Be led by your curiosity, and keep busy by doing things\nthat fill you with meaning and happiness. It doesn’t need to be a big thing: we\nmight find meaning in being good parents or in helping our neighbors.\nThere is no perfect strategy to connecting with our ikigai. But what we learned\nfrom the Okinawans is that we should not worry too much about finding it.\nLife is not a problem to be solved. Just remember to have something that\nkeeps you busy doing what you love while being surrounded by the people who\nlove you.\nThe ten rules of ikigai\nWe’ll conclude this journey with ten rules we’ve distilled from the wisdom of the\nlong-living residen', 'vector_score': 0.424901, 'hybrid_score': 0.4791543659896039}, {'id': 'ikigai.pdf__chunk_126', 'text': 'get to be so old.” When asked about his\nsecret to living so long, his answer was “I don’t know. I just haven’t died yet.”5\nIkigai artists\nThe secret to long life, however, is not held by supercentenarians alone. There are\nmany people of advanced age who, though they haven’t made it into Guinness\nWorld Records, offer us inspiration and ideas for bringing energy and meaning to\nour lives.\nArtists, for example, who carry the torch of their ikigai instead of retiring,\nhave this power.\nArt, in all its forms, is an ikigai that can bring happiness and purpose to our\ndays. Enjoying or creating beauty is free, and something all human beings have\naccess to.\nHokusai, the Japanese artist who made woodblock prints in the ukiyo-e style\nand lived for 88 years, from the mid-eighteenth to the mid-nineteenth century,\nadded this postscript to the first edition of his One Hundred Views of Mount\nFuji:6\nAll that I have produced before the age of 70 is not worth being counted. It is at the age of 73 that I\nha', 'vector_score': 0.42100051, 'hybrid_score': 0.4912996381371398}, {'id': 'ikigai.pdf__chunk_7', 'text': 'lobal average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet, a simple life in the outdoors, green tea, and the\nsubtropical climate (its average temperature is like that of Hawaii)—is the ikigai\nthat shapes their lives.\nWhile researching this concept, we discovered that not a single book in the\nfields of psychology or personal development is dedicated to bringing this\nphilosophy to the West.\nIs ikigai the reason there are more centenarians in Okinawa than anywhere\nelse? How does it inspire people to stay active until the very end? What is the\nsecret to a long and happy life?\nAs we explored the matter further, we discovered that one place in particular,\nOgimi, a rural town on the north end of the island with a population of three\nthousand, boasts the highest life expectancy in the world—a fact that has earned\nit the nickname the Village of Longevity.', 'vector_score': 0.416454345, 'hybrid_score': 0.5031255866000394}, {'id': 'ikigai.pdf__chunk_13', 'text': 'ntenarians from Okinawa and\nother so-called Blue Zones—the geographic regions where people live longest—\nprovide a number of interesting facts about these extraordinary human beings:\nNot only do they live much longer than the rest of the world’s population,\nthey also suffer from fewer chronic illnesses such as cancer and heart\ndisease; inflammatory disorders are also less common.\nMany of these centenarians enjoy enviable levels of vitality and health that\nwould be unthinkable for people of advanced age elsewhere.\nTheir blood tests reveal fewer free radicals (which are responsible for\ncellular aging), as a result of drinking tea and eating until their stomachs are\nonly 80 percent full.\nWomen experience more moderate symptoms during menopause, and both\nmen and women maintain higher levels of sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,”', 'vector_score': 0.414359123, 'hybrid_score': 0.4673649192465995}, {'id': 'ikigai.pdf__chunk_3', 'text': 'addresses, and other contact information at the\ntime of publication, neither the publisher nor the author assumes any responsibility for errors or for changes that occur after publication.\nFurther, the publisher does not have any control over and does not assume any responsibility for author or third-party Web sites or their\ncontent.\nCover illustration by Olga Grlic\nCover art direction by Roseanne Serra\nVersion_2\nFor my brother, Aitor,\nwho’s said to me more often than anyone else,\n“I don’t know what to do with my life.”\n—HÉCTOR GARCÍA\nFor all my past, present, and future friends,\nfor being my home and my motivation along\nthe way.\n—FRANCESC MIRALLES\nOnly staying active will make you want to live a hundred years.\n—Japanese proverb\nCONTENTS\nTitle Page\nCopyright\nDedication\nEpigraph\nPrologue\nIkigai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer', 'vector_score': 0.397349358, 'hybrid_score': 0.4919265126320816}, {'id': 'ikigai.pdf__chunk_65', 'text': 's on\nthree questions the individual must ask him-or herself:\n1. What have I received from person X?\n2. What have I given to person X?\n3. What problems have I caused person X?\nThrough these reflections, we stop identifying others as the cause of our\nproblems and deepen our own sense of responsibility. As Morita said, “If you are\nangry and want to fight, think about it for three days before coming to blows.\nAfter three days, the intense desire to fight will pass on its own.”7\nAnd now, ikigai\nLogotherapy and Morita therapy are both grounded in a personal, unique\nexperience that you can access without therapists or spiritual retreats: the mission\nof finding your ikigai, your existential fuel. Once you find it, it is only a matter of\nhaving the courage and making the effort to stay on the right path.\nIn the following chapters, we’ll take a look at the basic tools you’ll need to get\nmoving along that path: finding flow in the tasks you’ve chosen to do, eating in a\nbalanced and mindful way, d', 'vector_score': 0.38858512, 'hybrid_score': 0.4602721291659915}, {'id': 'ikigai.pdf__chunk_21', 'text': 'o the group. This\npayment allows them to participate in meetings, dinners, games of go and shogi\n(Japanese chess), or whatever hobby they have in common.\nThe funds collected by the group are used for activities, but if there is money\nleft over, one member (decided on a rotating basis) receives a set amount from\nthe surplus. In this way, being part of a moai helps maintain emotional and\nfinancial stability. If a member of a moai is in financial trouble, he or she can get\nan advance from the group’s savings. While the details of each moai’s accounting\npractices vary according to the group and its economic means, the feeling of\nbelonging and support gives the individual a sense of security and helps increase\nlife expectancy.\n• • •\nFOLLOWING THIS BRIEF introduction to the topics covered in this book, we look at\na few causes of premature aging in modern life, and then explore different\nfactors related to ikigai.\nII\nANTIAGING SECRETS\nLittle things that add up to a long\nand happy life\nAging’s', 'vector_score': 0.388457298, 'hybrid_score': 0.2913429735}, {'id': 'ikigai.pdf__chunk_17', 'text': 'it is worth\npointing out that three of these regions are islands, where resources can be scarce\nand communities have to help one another.\nFor many, helping others might be an ikigai strong enough to keep them alive.\nAccording to scientists who have studied the five Blue Zones, the keys to\nlongevity are diet, exercise, finding a purpose in life (an ikigai), and forming\nstrong social ties—that is, having a broad circle of friends and good family\nrelations.\nMembers of these communities manage their time well in order to reduce\nstress, consume little meat or processed foods, and drink alcohol in moderation.1\nThey don’t do strenuous exercise, but they do move every day, taking walks\nand working in their vegetable gardens. People in the Blue Zones would rather\nwalk than drive. Gardening, which involves daily low-intensity movement, is a\npractice almost all of them have in common.\nThe 80 percent secret\nOne of the most common sayings in Japan is “Hara hachi bu,” which is repeated\nbefore or aft', 'vector_score': 0.364305973, 'hybrid_score': 0.38058252422688743}, {'id': 'ikigai.pdf__chunk_1', 'text': 'All other illustrations copyright © 2016 by Marisa Martínez Graphics copyright © 2016 by Flora\nBuki\nLIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Names: García, Héctor, 1981– author. | Miralles, Francesc, 1968– author.\nTitle: Ikigai : the Japanese secret to a long and happy life / Héctor García and Francesc Miralles ; translated by Heather Cleary.\nOther titles: Ikigai. English\nDescription: New York : Penguin Books, [2017] | Originally published in Spanish as “Ikigai: Los secretos de Japón para una vida larga y\nfeliz” by Ediciones Urano in 2016." | Includes bibliographical references. | Description based on print version record and CIP data\nprovided by publisher; resource not viewed.\nIdentifiers: LCCN 2017005811 (print) | LCCN 2017022599 (ebook) | ISBN 9781524704551 (ebook) | ISBN 9780143130727\n(hardcover) Subjects: LCSH: Longevity—Japan. | Longevity. | Happiness. | Quality of life Classification: LCC RA776.75 (ebook) | LCC\nRA776.75 .G3713 2017 (print) | DDC 613—dc23\nLC record ava', 'vector_score': 0.356697083, 'hybrid_score': 0.38054549102005464}, {'id': 'ikigai.pdf__chunk_154', 'text': 'ential parts of daily life.\nThey have an important purpose in life, or several. They have an ikigai,\nbut they don’t take it too seriously. They are relaxed and enjoy all that\nthey do.\nThey are very proud of their traditions and local culture.\nThey are passionate about everything they do, however insignificant it\nmight seem.\nLocals have a strong sense of yuimaaru—recognizing the connection\nbetween people. They help each other with everything from work in the\nfields (harvesting sugarcane or planting rice) to building houses and\nmunicipal projects. Our friend Miyagi, who ate dinner with us on our\nlast night in town, told us that he was building a new home with the help\nof all his friends, and that we could stay there the next time we were in\nOgimi.\nThey are always busy, but they occupy themselves with tasks that allow\nthem to relax. We didn’t see a single old grandpa sitting on a bench\ndoing nothing. They’re always coming and going—to sing karaoke, visit\nwith neighbors, or play a game of', 'vector_score': 0.354898453, 'hybrid_score': 0.26617383975}]

chunk_texts: ['e a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru, or\nteamwork, and so are used to helping one another.\nNurturing friendships, eating light, getting enough rest, and doing regular,\nmoderate exercise are all part of the equation of good health, but at the heart of\nthe joie de vivre that inspires these centenarians to keep celebrating birthdays and\ncherishing each new day is their ikigai.\nThe purpose of this book is to bring the secrets of Japan’s centenarians to you\nand give you the tools to find your own ikigai.\nBecause those who discover their ikigai have everything they need for a long\nand joyful journey through life.\nHappy travels!\nHÉCTOR GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call', 'igai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer and better by finding your purpose\nIV. Find Flow in Everything You Do\nHow to turn work and free time into spaces for growth\nV. Masters of Longevity\nWords of wisdom from the longest-living people in the world\nVI. Lessons from Japan’s Centenarians\nTraditions and proverbs for happiness and longevity\nVII. The Ikigai Diet\nWhat the world’s longest-living people eat and drink\nVIII. Gentle Movements, Longer Life\nExercises from the East that promote health and longevity\nIX. Resilience and Wabi-sabi\nHow to face life’s challenges without letting stress and worry age you\nEpilogue\nIkigai: The art of living\nNotes\nSuggestions for further reading\nAbout the Authors\nPROLOGUE\nIkigai: A mysterious word\nTHIS BOOK FIRST came into being on a rainy night in Tokyo, when its authors sat\ndown together for the first', 'GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call a raison d’être. Some people have found their ikigai, while others are\nstill looking, though they carry it within them.\nOur ikigai is hidden deep inside each of us, and finding it requires a patient\nsearch. According to those born on Okinawa, the island with the most\ncentenarians in the world, our ikigai is the reason we get up in the morning.\nWhatever you do, don’t retire!\nHaving a clearly defined ikigai brings satisfaction, happiness, and meaning to our\nlives. The purpose of this book is to help you find yours, and to share insights\nfrom Japanese philosophy on the lasting health of body, mind, and spirit.\nOne surprising thing you notice, living in Japan, is how active people remain\nafter they retire. In fact, many Japanese people never really retire—they keep\ndoing what they love for as', 'liness of its residents,\nwho laughed and joked incessantly amid lush green hills fed by crystalline waters.\nAs we conducted our interviews with the eldest residents of the town, we\nrealized that something far more powerful than just these natural resources was at\nwork: an uncommon joy flows from its inhabitants and guides them through the\nlong and pleasurable journey of their lives.\nAgain, the mysterious ikigai.\nBut what is it, exactly? How do you get it?\nIt never ceased to surprise us that this haven of nearly eternal life was located\nprecisely in Okinawa, where two hundred thousand innocent lives were lost at the\nend of World War II. Rather than harbor animosity toward outsiders, however,\nOkinawans live by the principle of ichariba chode, a local expression that means\n“treat everyone like a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru', 'sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,” with 甲斐, which means “to be worthwhile.” 甲斐 can be broken\ndown into the characters 甲, which means “armor,” “number one,” and “to\nbe the first” (to head into battle, taking initiative as a leader), and 斐,\nwhich means “beautiful” or “elegant.”\nThough we will consider each of these findings over the course of the book,\nresearch clearly indicates that the Okinawans’ focus on ikigai gives a sense of\npurpose to each and every day and plays an important role in their health and\nlongevity.\nThe five Blue Zones\nOkinawa holds first place among the world’s Blue Zones. In Okinawa, women in\nparticular live longer and have fewer diseases than anywhere else in the world.\nThe five regions identified and analyzed by Dan Buettner in his book The Blue\nZones are:\n1. Okinawa, Japan (especially the northern par', 'e, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing it every day will bring\nmeaning to your life. The moment your life has this purpose, you will achieve a\nhappy state of flow in all you do, like the calligrapher at his canvas or the chef\nwho, after half a century, still prepares sushi for his patrons with love.\nConclusion\nOur ikigai is different for all of us, but one thing we have in common is that we\nare all searching for meaning. When we spend our days feeling connected to what\nis meaningful to us, we live more fully; when we lose the connection, we feel\ndespair.\nModern life estranges us more and more from our true nature, making it very\neasy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curio', 'keaway is that they all combine a physical\nexercise with an awareness of our breath. These two components—movement\nand breath—help us to bring our consciousness in line with our body, instead of\nallowing our mind to be carried away by the sea of daily worries. Most of the\ntime, we are just not aware enough of our breathing.\nIX\nRESILIENCE AND WABI-SABI\nHow to face life’s challenges\nwithout letting stress and worry age\nyou\nWhat is resilience?\nOne thing that everyone with a clearly defined ikigai has in common is that they\npursue their passion no matter what. They never give up, even when the cards\nseem stacked against them or they face one hurdle after another.\nWe’re talking about resilience, a concept that has become influential among\npsychologists.\nBut resilience isn’t just the ability to persevere. As we’ll see in this chapter, it\nis also an outlook we can cultivate to stay focused on the important things in life\nrather than what is most urgent, and to keep ourselves from being carrie', 'igraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems, using a shodo calligraphy brush.\nMany of Aida’s haikus philosophize about the importance of the present\nmoment, and the passage of time. The poem reproduced below could be\ntranslated as “In the here and now, the only thing in my life is your life.”\nいまここにしかないわたし\nのいのちあなたのいのち\nIn another poem, Aida writes simply, “Here, now.” It is an artwork that seeks\nto evoke feelings of mono no aware (a melancholy appreciation of the\nephemeral).\nいまここ\nThe following poem touches on one of the secrets of bringing ikigai into our\nlives: “Happiness is always determined by your heart.”\nしあわせはいつも自分の心がきめる\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing', 'cticing therapists, who favored other schools of psychology, though people\nstill search for meaning in what they do and how they live. We ask ourselves\nthings like:\nWhat is the meaning of my life?\nIs the point just to live longer, or should I seek a higher purpose?\nWhy do some people know what they want and have a passion for life, while\nothers languish in confusion?\nAt some point in our conversation, the mysterious word ikigai came up.\nThis Japanese concept, which translates roughly as “the happiness of always\nbeing busy,” is like logotherapy, but it goes a step beyond. It also seems to be one\nway of explaining the extraordinary longevity of the Japanese, especially on the\nisland of Okinawa, where there are 24.55 people over the age of 100 for every\n100,000 inhabitants—far more than the global average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet,', 'hit or two can be viewed as either a misfortune or an experience that\nwe can apply to all areas of our lives, as we continually make corrections and set\nnew and better goals. As Taleb writes in Antifragile, “We need randomness, mess,\nadventures, uncertainty, self-discovery, hear traumatic episodes, all these things\nthat make life worth living.” We encourage those interested in the concept of\nantifragility to read Nassim Nicholas Taleb’s Antifragile.\nLife is pure imperfection, as the philosophy of wabi-sabi teaches us, and the\npassage of time shows us that everything is fleeting, but if you have a clear sense\nof your ikigai, each moment will hold so many possibilities that it will seem\nalmost like an eternity.\nEPILOGUE\nIkigai: The art of living\nMitsuo Aida was one of the most important calligraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems,', 'asy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curiosity are very powerful internal compasses to help us\nconnect with our ikigai. Follow those things you enjoy, and get away from or\nchange those you dislike. Be led by your curiosity, and keep busy by doing things\nthat fill you with meaning and happiness. It doesn’t need to be a big thing: we\nmight find meaning in being good parents or in helping our neighbors.\nThere is no perfect strategy to connecting with our ikigai. But what we learned\nfrom the Okinawans is that we should not worry too much about finding it.\nLife is not a problem to be solved. Just remember to have something that\nkeeps you busy doing what you love while being surrounded by the people who\nlove you.\nThe ten rules of ikigai\nWe’ll conclude this journey with ten rules we’ve distilled from the wisdom of the\nlong-living residen', 'get to be so old.” When asked about his\nsecret to living so long, his answer was “I don’t know. I just haven’t died yet.”5\nIkigai artists\nThe secret to long life, however, is not held by supercentenarians alone. There are\nmany people of advanced age who, though they haven’t made it into Guinness\nWorld Records, offer us inspiration and ideas for bringing energy and meaning to\nour lives.\nArtists, for example, who carry the torch of their ikigai instead of retiring,\nhave this power.\nArt, in all its forms, is an ikigai that can bring happiness and purpose to our\ndays. Enjoying or creating beauty is free, and something all human beings have\naccess to.\nHokusai, the Japanese artist who made woodblock prints in the ukiyo-e style\nand lived for 88 years, from the mid-eighteenth to the mid-nineteenth century,\nadded this postscript to the first edition of his One Hundred Views of Mount\nFuji:6\nAll that I have produced before the age of 70 is not worth being counted. It is at the age of 73 that I\nha', 'lobal average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet, a simple life in the outdoors, green tea, and the\nsubtropical climate (its average temperature is like that of Hawaii)—is the ikigai\nthat shapes their lives.\nWhile researching this concept, we discovered that not a single book in the\nfields of psychology or personal development is dedicated to bringing this\nphilosophy to the West.\nIs ikigai the reason there are more centenarians in Okinawa than anywhere\nelse? How does it inspire people to stay active until the very end? What is the\nsecret to a long and happy life?\nAs we explored the matter further, we discovered that one place in particular,\nOgimi, a rural town on the north end of the island with a population of three\nthousand, boasts the highest life expectancy in the world—a fact that has earned\nit the nickname the Village of Longevity.', 'ntenarians from Okinawa and\nother so-called Blue Zones—the geographic regions where people live longest—\nprovide a number of interesting facts about these extraordinary human beings:\nNot only do they live much longer than the rest of the world’s population,\nthey also suffer from fewer chronic illnesses such as cancer and heart\ndisease; inflammatory disorders are also less common.\nMany of these centenarians enjoy enviable levels of vitality and health that\nwould be unthinkable for people of advanced age elsewhere.\nTheir blood tests reveal fewer free radicals (which are responsible for\ncellular aging), as a result of drinking tea and eating until their stomachs are\nonly 80 percent full.\nWomen experience more moderate symptoms during menopause, and both\nmen and women maintain higher levels of sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,”', 'addresses, and other contact information at the\ntime of publication, neither the publisher nor the author assumes any responsibility for errors or for changes that occur after publication.\nFurther, the publisher does not have any control over and does not assume any responsibility for author or third-party Web sites or their\ncontent.\nCover illustration by Olga Grlic\nCover art direction by Roseanne Serra\nVersion_2\nFor my brother, Aitor,\nwho’s said to me more often than anyone else,\n“I don’t know what to do with my life.”\n—HÉCTOR GARCÍA\nFor all my past, present, and future friends,\nfor being my home and my motivation along\nthe way.\n—FRANCESC MIRALLES\nOnly staying active will make you want to live a hundred years.\n—Japanese proverb\nCONTENTS\nTitle Page\nCopyright\nDedication\nEpigraph\nPrologue\nIkigai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer', 's on\nthree questions the individual must ask him-or herself:\n1. What have I received from person X?\n2. What have I given to person X?\n3. What problems have I caused person X?\nThrough these reflections, we stop identifying others as the cause of our\nproblems and deepen our own sense of responsibility. As Morita said, “If you are\nangry and want to fight, think about it for three days before coming to blows.\nAfter three days, the intense desire to fight will pass on its own.”7\nAnd now, ikigai\nLogotherapy and Morita therapy are both grounded in a personal, unique\nexperience that you can access without therapists or spiritual retreats: the mission\nof finding your ikigai, your existential fuel. Once you find it, it is only a matter of\nhaving the courage and making the effort to stay on the right path.\nIn the following chapters, we’ll take a look at the basic tools you’ll need to get\nmoving along that path: finding flow in the tasks you’ve chosen to do, eating in a\nbalanced and mindful way, d', 'o the group. This\npayment allows them to participate in meetings, dinners, games of go and shogi\n(Japanese chess), or whatever hobby they have in common.\nThe funds collected by the group are used for activities, but if there is money\nleft over, one member (decided on a rotating basis) receives a set amount from\nthe surplus. In this way, being part of a moai helps maintain emotional and\nfinancial stability. If a member of a moai is in financial trouble, he or she can get\nan advance from the group’s savings. While the details of each moai’s accounting\npractices vary according to the group and its economic means, the feeling of\nbelonging and support gives the individual a sense of security and helps increase\nlife expectancy.\n• • •\nFOLLOWING THIS BRIEF introduction to the topics covered in this book, we look at\na few causes of premature aging in modern life, and then explore different\nfactors related to ikigai.\nII\nANTIAGING SECRETS\nLittle things that add up to a long\nand happy life\nAging’s', 'it is worth\npointing out that three of these regions are islands, where resources can be scarce\nand communities have to help one another.\nFor many, helping others might be an ikigai strong enough to keep them alive.\nAccording to scientists who have studied the five Blue Zones, the keys to\nlongevity are diet, exercise, finding a purpose in life (an ikigai), and forming\nstrong social ties—that is, having a broad circle of friends and good family\nrelations.\nMembers of these communities manage their time well in order to reduce\nstress, consume little meat or processed foods, and drink alcohol in moderation.1\nThey don’t do strenuous exercise, but they do move every day, taking walks\nand working in their vegetable gardens. People in the Blue Zones would rather\nwalk than drive. Gardening, which involves daily low-intensity movement, is a\npractice almost all of them have in common.\nThe 80 percent secret\nOne of the most common sayings in Japan is “Hara hachi bu,” which is repeated\nbefore or aft', 'All other illustrations copyright © 2016 by Marisa Martínez Graphics copyright © 2016 by Flora\nBuki\nLIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Names: García, Héctor, 1981– author. | Miralles, Francesc, 1968– author.\nTitle: Ikigai : the Japanese secret to a long and happy life / Héctor García and Francesc Miralles ; translated by Heather Cleary.\nOther titles: Ikigai. English\nDescription: New York : Penguin Books, [2017] | Originally published in Spanish as “Ikigai: Los secretos de Japón para una vida larga y\nfeliz” by Ediciones Urano in 2016." | Includes bibliographical references. | Description based on print version record and CIP data\nprovided by publisher; resource not viewed.\nIdentifiers: LCCN 2017005811 (print) | LCCN 2017022599 (ebook) | ISBN 9781524704551 (ebook) | ISBN 9780143130727\n(hardcover) Subjects: LCSH: Longevity—Japan. | Longevity. | Happiness. | Quality of life Classification: LCC RA776.75 (ebook) | LCC\nRA776.75 .G3713 2017 (print) | DDC 613—dc23\nLC record ava', 'ential parts of daily life.\nThey have an important purpose in life, or several. They have an ikigai,\nbut they don’t take it too seriously. They are relaxed and enjoy all that\nthey do.\nThey are very proud of their traditions and local culture.\nThey are passionate about everything they do, however insignificant it\nmight seem.\nLocals have a strong sense of yuimaaru—recognizing the connection\nbetween people. They help each other with everything from work in the\nfields (harvesting sugarcane or planting rice) to building houses and\nmunicipal projects. Our friend Miyagi, who ate dinner with us on our\nlast night in town, told us that he was building a new home with the help\nof all his friends, and that we could stay there the next time we were in\nOgimi.\nThey are always busy, but they occupy themselves with tasks that allow\nthem to relax. We didn’t see a single old grandpa sitting on a bench\ndoing nothing. They’re always coming and going—to sing karaoke, visit\nwith neighbors, or play a game of']

reranker_scores: [3.3388073 6.2908225 6.2895923 3.4461205 5.818521  4.0708222 1.9220674
 3.7930381 3.960894  1.5804836 2.256405  3.864362  3.661822  3.2327151
 3.23114   1.5289533 0.6934171 2.464394  5.5371337 1.6774462]

candidates: [{'id': 'ikigai.pdf__chunk_4', 'text': 'igai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer and better by finding your purpose\nIV. Find Flow in Everything You Do\nHow to turn work and free time into spaces for growth\nV. Masters of Longevity\nWords of wisdom from the longest-living people in the world\nVI. Lessons from Japan’s Centenarians\nTraditions and proverbs for happiness and longevity\nVII. The Ikigai Diet\nWhat the world’s longest-living people eat and drink\nVIII. Gentle Movements, Longer Life\nExercises from the East that promote health and longevity\nIX. Resilience and Wabi-sabi\nHow to face life’s challenges without letting stress and worry age you\nEpilogue\nIkigai: The art of living\nNotes\nSuggestions for further reading\nAbout the Authors\nPROLOGUE\nIkigai: A mysterious word\nTHIS BOOK FIRST came into being on a rainy night in Tokyo, when its authors sat\ndown together for the first', 'vector_score': 0.530410767, 'hybrid_score': 0.6158509090777831, 'rerank_score': 6.290822505950928}, {'id': 'ikigai.pdf__chunk_11', 'text': 'GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call a raison d’être. Some people have found their ikigai, while others are\nstill looking, though they carry it within them.\nOur ikigai is hidden deep inside each of us, and finding it requires a patient\nsearch. According to those born on Okinawa, the island with the most\ncentenarians in the world, our ikigai is the reason we get up in the morning.\nWhatever you do, don’t retire!\nHaving a clearly defined ikigai brings satisfaction, happiness, and meaning to our\nlives. The purpose of this book is to help you find yours, and to share insights\nfrom Japanese philosophy on the lasting health of body, mind, and spirit.\nOne surprising thing you notice, living in Japan, is how active people remain\nafter they retire. In fact, many Japanese people never really retire—they keep\ndoing what they love for as', 'vector_score': 0.527626038, 'hybrid_score': 0.6457195284999999, 'rerank_score': 6.289592266082764}, {'id': 'ikigai.pdf__chunk_14', 'text': 'sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,” with 甲斐, which means “to be worthwhile.” 甲斐 can be broken\ndown into the characters 甲, which means “armor,” “number one,” and “to\nbe the first” (to head into battle, taking initiative as a leader), and 斐,\nwhich means “beautiful” or “elegant.”\nThough we will consider each of these findings over the course of the book,\nresearch clearly indicates that the Okinawans’ focus on ikigai gives a sense of\npurpose to each and every day and plays an important role in their health and\nlongevity.\nThe five Blue Zones\nOkinawa holds first place among the world’s Blue Zones. In Okinawa, women in\nparticular live longer and have fewer diseases than anywhere else in the world.\nThe five regions identified and analyzed by Dan Buettner in his book The Blue\nZones are:\n1. Okinawa, Japan (especially the northern par', 'vector_score': 0.482807666, 'hybrid_score': 0.5399585809756482, 'rerank_score': 5.818521022796631}, {'id': 'ikigai.pdf__chunk_1', 'text': 'All other illustrations copyright © 2016 by Marisa Martínez Graphics copyright © 2016 by Flora\nBuki\nLIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Names: García, Héctor, 1981– author. | Miralles, Francesc, 1968– author.\nTitle: Ikigai : the Japanese secret to a long and happy life / Héctor García and Francesc Miralles ; translated by Heather Cleary.\nOther titles: Ikigai. English\nDescription: New York : Penguin Books, [2017] | Originally published in Spanish as “Ikigai: Los secretos de Japón para una vida larga y\nfeliz” by Ediciones Urano in 2016." | Includes bibliographical references. | Description based on print version record and CIP data\nprovided by publisher; resource not viewed.\nIdentifiers: LCCN 2017005811 (print) | LCCN 2017022599 (ebook) | ISBN 9781524704551 (ebook) | ISBN 9780143130727\n(hardcover) Subjects: LCSH: Longevity—Japan. | Longevity. | Happiness. | Quality of life Classification: LCC RA776.75 (ebook) | LCC\nRA776.75 .G3713 2017 (print) | DDC 613—dc23\nLC record ava', 'vector_score': 0.356697083, 'hybrid_score': 0.38054549102005464, 'rerank_score': 5.537133693695068}, {'id': 'ikigai.pdf__chunk_221', 'text': 'e, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing it every day will bring\nmeaning to your life. The moment your life has this purpose, you will achieve a\nhappy state of flow in all you do, like the calligrapher at his canvas or the chef\nwho, after half a century, still prepares sushi for his patrons with love.\nConclusion\nOur ikigai is different for all of us, but one thing we have in common is that we\nare all searching for meaning. When we spend our days feeling connected to what\nis meaningful to us, we live more fully; when we lose the connection, we feel\ndespair.\nModern life estranges us more and more from our true nature, making it very\neasy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curio', 'vector_score': 0.457759857, 'hybrid_score': 0.4858278169209863, 'rerank_score': 4.070822238922119}, {'id': 'ikigai.pdf__chunk_6', 'text': 'cticing therapists, who favored other schools of psychology, though people\nstill search for meaning in what they do and how they live. We ask ourselves\nthings like:\nWhat is the meaning of my life?\nIs the point just to live longer, or should I seek a higher purpose?\nWhy do some people know what they want and have a passion for life, while\nothers languish in confusion?\nAt some point in our conversation, the mysterious word ikigai came up.\nThis Japanese concept, which translates roughly as “the happiness of always\nbeing busy,” is like logotherapy, but it goes a step beyond. It also seems to be one\nway of explaining the extraordinary longevity of the Japanese, especially on the\nisland of Okinawa, where there are 24.55 people over the age of 100 for every\n100,000 inhabitants—far more than the global average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet,', 'vector_score': 0.438530922, 'hybrid_score': 0.499917536604492, 'rerank_score': 3.9608941078186035}, {'id': 'ikigai.pdf__chunk_126', 'text': 'get to be so old.” When asked about his\nsecret to living so long, his answer was “I don’t know. I just haven’t died yet.”5\nIkigai artists\nThe secret to long life, however, is not held by supercentenarians alone. There are\nmany people of advanced age who, though they haven’t made it into Guinness\nWorld Records, offer us inspiration and ideas for bringing energy and meaning to\nour lives.\nArtists, for example, who carry the torch of their ikigai instead of retiring,\nhave this power.\nArt, in all its forms, is an ikigai that can bring happiness and purpose to our\ndays. Enjoying or creating beauty is free, and something all human beings have\naccess to.\nHokusai, the Japanese artist who made woodblock prints in the ukiyo-e style\nand lived for 88 years, from the mid-eighteenth to the mid-nineteenth century,\nadded this postscript to the first edition of his One Hundred Views of Mount\nFuji:6\nAll that I have produced before the age of 70 is not worth being counted. It is at the age of 73 that I\nha', 'vector_score': 0.42100051, 'hybrid_score': 0.4912996381371398, 'rerank_score': 3.8643620014190674}, {'id': 'ikigai.pdf__chunk_220', 'text': 'igraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems, using a shodo calligraphy brush.\nMany of Aida’s haikus philosophize about the importance of the present\nmoment, and the passage of time. The poem reproduced below could be\ntranslated as “In the here and now, the only thing in my life is your life.”\nいまここにしかないわたし\nのいのちあなたのいのち\nIn another poem, Aida writes simply, “Here, now.” It is an artwork that seeks\nto evoke feelings of mono no aware (a melancholy appreciation of the\nephemeral).\nいまここ\nThe following poem touches on one of the secrets of bringing ikigai into our\nlives: “Happiness is always determined by your heart.”\nしあわせはいつも自分の心がきめる\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nThis last one, also by Aida, means “Keep going; don’t change your path.”\nそのままでいいがな\nOnce you discover your ikigai, pursuing it and nurturing', 'vector_score': 0.44162178, 'hybrid_score': 0.4402973497589044, 'rerank_score': 3.7930381298065186}, {'id': 'ikigai.pdf__chunk_7', 'text': 'lobal average.\nThose who study why the inhabitants of this island in the south of Japan live\nlonger than people anywhere else in the world believe that one of the keys—in\naddition to a healthful diet, a simple life in the outdoors, green tea, and the\nsubtropical climate (its average temperature is like that of Hawaii)—is the ikigai\nthat shapes their lives.\nWhile researching this concept, we discovered that not a single book in the\nfields of psychology or personal development is dedicated to bringing this\nphilosophy to the West.\nIs ikigai the reason there are more centenarians in Okinawa than anywhere\nelse? How does it inspire people to stay active until the very end? What is the\nsecret to a long and happy life?\nAs we explored the matter further, we discovered that one place in particular,\nOgimi, a rural town on the north end of the island with a population of three\nthousand, boasts the highest life expectancy in the world—a fact that has earned\nit the nickname the Village of Longevity.', 'vector_score': 0.416454345, 'hybrid_score': 0.5031255866000394, 'rerank_score': 3.6618220806121826}, {'id': 'ikigai.pdf__chunk_9', 'text': 'liness of its residents,\nwho laughed and joked incessantly amid lush green hills fed by crystalline waters.\nAs we conducted our interviews with the eldest residents of the town, we\nrealized that something far more powerful than just these natural resources was at\nwork: an uncommon joy flows from its inhabitants and guides them through the\nlong and pleasurable journey of their lives.\nAgain, the mysterious ikigai.\nBut what is it, exactly? How do you get it?\nIt never ceased to surprise us that this haven of nearly eternal life was located\nprecisely in Okinawa, where two hundred thousand innocent lives were lost at the\nend of World War II. Rather than harbor animosity toward outsiders, however,\nOkinawans live by the principle of ichariba chode, a local expression that means\n“treat everyone like a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru', 'vector_score': 0.524535239, 'hybrid_score': 0.43307129183940196, 'rerank_score': 3.446120500564575}, {'id': 'ikigai.pdf__chunk_10', 'text': 'e a brother, even if you’ve never met them before.”\nIt turns out that one of the secrets to happiness of Ogimi’s residents is feeling\nlike part of a community. From an early age they practice yuimaaru, or\nteamwork, and so are used to helping one another.\nNurturing friendships, eating light, getting enough rest, and doing regular,\nmoderate exercise are all part of the equation of good health, but at the heart of\nthe joie de vivre that inspires these centenarians to keep celebrating birthdays and\ncherishing each new day is their ikigai.\nThe purpose of this book is to bring the secrets of Japan’s centenarians to you\nand give you the tools to find your own ikigai.\nBecause those who discover their ikigai have everything they need for a long\nand joyful journey through life.\nHappy travels!\nHÉCTOR GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call', 'vector_score': 0.568400383, 'hybrid_score': 0.6174706647148859, 'rerank_score': 3.3388073444366455}, {'id': 'ikigai.pdf__chunk_13', 'text': 'ntenarians from Okinawa and\nother so-called Blue Zones—the geographic regions where people live longest—\nprovide a number of interesting facts about these extraordinary human beings:\nNot only do they live much longer than the rest of the world’s population,\nthey also suffer from fewer chronic illnesses such as cancer and heart\ndisease; inflammatory disorders are also less common.\nMany of these centenarians enjoy enviable levels of vitality and health that\nwould be unthinkable for people of advanced age elsewhere.\nTheir blood tests reveal fewer free radicals (which are responsible for\ncellular aging), as a result of drinking tea and eating until their stomachs are\nonly 80 percent full.\nWomen experience more moderate symptoms during menopause, and both\nmen and women maintain higher levels of sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,”', 'vector_score': 0.414359123, 'hybrid_score': 0.4673649192465995, 'rerank_score': 3.232715129852295}, {'id': 'ikigai.pdf__chunk_3', 'text': 'addresses, and other contact information at the\ntime of publication, neither the publisher nor the author assumes any responsibility for errors or for changes that occur after publication.\nFurther, the publisher does not have any control over and does not assume any responsibility for author or third-party Web sites or their\ncontent.\nCover illustration by Olga Grlic\nCover art direction by Roseanne Serra\nVersion_2\nFor my brother, Aitor,\nwho’s said to me more often than anyone else,\n“I don’t know what to do with my life.”\n—HÉCTOR GARCÍA\nFor all my past, present, and future friends,\nfor being my home and my motivation along\nthe way.\n—FRANCESC MIRALLES\nOnly staying active will make you want to live a hundred years.\n—Japanese proverb\nCONTENTS\nTitle Page\nCopyright\nDedication\nEpigraph\nPrologue\nIkigai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer', 'vector_score': 0.397349358, 'hybrid_score': 0.4919265126320816, 'rerank_score': 3.231139898300171}, {'id': 'ikigai.pdf__chunk_17', 'text': 'it is worth\npointing out that three of these regions are islands, where resources can be scarce\nand communities have to help one another.\nFor many, helping others might be an ikigai strong enough to keep them alive.\nAccording to scientists who have studied the five Blue Zones, the keys to\nlongevity are diet, exercise, finding a purpose in life (an ikigai), and forming\nstrong social ties—that is, having a broad circle of friends and good family\nrelations.\nMembers of these communities manage their time well in order to reduce\nstress, consume little meat or processed foods, and drink alcohol in moderation.1\nThey don’t do strenuous exercise, but they do move every day, taking walks\nand working in their vegetable gardens. People in the Blue Zones would rather\nwalk than drive. Gardening, which involves daily low-intensity movement, is a\npractice almost all of them have in common.\nThe 80 percent secret\nOne of the most common sayings in Japan is “Hara hachi bu,” which is repeated\nbefore or aft', 'vector_score': 0.364305973, 'hybrid_score': 0.38058252422688743, 'rerank_score': 2.4643940925598145}, {'id': 'ikigai.pdf__chunk_222', 'text': 'asy for us to lead lives lacking in meaning. Powerful forces and incentives\n(money, power, attention, success) distract us on a daily basis; don’t let them take\nover your life.\nOur intuition and curiosity are very powerful internal compasses to help us\nconnect with our ikigai. Follow those things you enjoy, and get away from or\nchange those you dislike. Be led by your curiosity, and keep busy by doing things\nthat fill you with meaning and happiness. It doesn’t need to be a big thing: we\nmight find meaning in being good parents or in helping our neighbors.\nThere is no perfect strategy to connecting with our ikigai. But what we learned\nfrom the Okinawans is that we should not worry too much about finding it.\nLife is not a problem to be solved. Just remember to have something that\nkeeps you busy doing what you love while being surrounded by the people who\nlove you.\nThe ten rules of ikigai\nWe’ll conclude this journey with ten rules we’ve distilled from the wisdom of the\nlong-living residen', 'vector_score': 0.424901, 'hybrid_score': 0.4791543659896039, 'rerank_score': 2.2564051151275635}, {'id': 'ikigai.pdf__chunk_197', 'text': 'keaway is that they all combine a physical\nexercise with an awareness of our breath. These two components—movement\nand breath—help us to bring our consciousness in line with our body, instead of\nallowing our mind to be carried away by the sea of daily worries. Most of the\ntime, we are just not aware enough of our breathing.\nIX\nRESILIENCE AND WABI-SABI\nHow to face life’s challenges\nwithout letting stress and worry age\nyou\nWhat is resilience?\nOne thing that everyone with a clearly defined ikigai has in common is that they\npursue their passion no matter what. They never give up, even when the cards\nseem stacked against them or they face one hurdle after another.\nWe’re talking about resilience, a concept that has become influential among\npsychologists.\nBut resilience isn’t just the ability to persevere. As we’ll see in this chapter, it\nis also an outlook we can cultivate to stay focused on the important things in life\nrather than what is most urgent, and to keep ourselves from being carrie', 'vector_score': 0.443742752, 'hybrid_score': 0.49517496918069626, 'rerank_score': 1.922067403793335}, {'id': 'ikigai.pdf__chunk_154', 'text': 'ential parts of daily life.\nThey have an important purpose in life, or several. They have an ikigai,\nbut they don’t take it too seriously. They are relaxed and enjoy all that\nthey do.\nThey are very proud of their traditions and local culture.\nThey are passionate about everything they do, however insignificant it\nmight seem.\nLocals have a strong sense of yuimaaru—recognizing the connection\nbetween people. They help each other with everything from work in the\nfields (harvesting sugarcane or planting rice) to building houses and\nmunicipal projects. Our friend Miyagi, who ate dinner with us on our\nlast night in town, told us that he was building a new home with the help\nof all his friends, and that we could stay there the next time we were in\nOgimi.\nThey are always busy, but they occupy themselves with tasks that allow\nthem to relax. We didn’t see a single old grandpa sitting on a bench\ndoing nothing. They’re always coming and going—to sing karaoke, visit\nwith neighbors, or play a game of', 'vector_score': 0.354898453, 'hybrid_score': 0.26617383975, 'rerank_score': 1.6774462461471558}, {'id': 'ikigai.pdf__chunk_219', 'text': 'hit or two can be viewed as either a misfortune or an experience that\nwe can apply to all areas of our lives, as we continually make corrections and set\nnew and better goals. As Taleb writes in Antifragile, “We need randomness, mess,\nadventures, uncertainty, self-discovery, hear traumatic episodes, all these things\nthat make life worth living.” We encourage those interested in the concept of\nantifragility to read Nassim Nicholas Taleb’s Antifragile.\nLife is pure imperfection, as the philosophy of wabi-sabi teaches us, and the\npassage of time shows us that everything is fleeting, but if you have a clear sense\nof your ikigai, each moment will hold so many possibilities that it will seem\nalmost like an eternity.\nEPILOGUE\nIkigai: The art of living\nMitsuo Aida was one of the most important calligraphers and haikuists of the\ntwentieth century. He is yet another example of a Japanese person who dedicated\nhis life to a very specific ikigai: communicating emotions with seventeen-syllable\npoems,', 'vector_score': 0.43230629, 'hybrid_score': 0.32422971749999996, 'rerank_score': 1.5804835557937622}, {'id': 'ikigai.pdf__chunk_65', 'text': 's on\nthree questions the individual must ask him-or herself:\n1. What have I received from person X?\n2. What have I given to person X?\n3. What problems have I caused person X?\nThrough these reflections, we stop identifying others as the cause of our\nproblems and deepen our own sense of responsibility. As Morita said, “If you are\nangry and want to fight, think about it for three days before coming to blows.\nAfter three days, the intense desire to fight will pass on its own.”7\nAnd now, ikigai\nLogotherapy and Morita therapy are both grounded in a personal, unique\nexperience that you can access without therapists or spiritual retreats: the mission\nof finding your ikigai, your existential fuel. Once you find it, it is only a matter of\nhaving the courage and making the effort to stay on the right path.\nIn the following chapters, we’ll take a look at the basic tools you’ll need to get\nmoving along that path: finding flow in the tasks you’ve chosen to do, eating in a\nbalanced and mindful way, d', 'vector_score': 0.38858512, 'hybrid_score': 0.4602721291659915, 'rerank_score': 1.5289533138275146}, {'id': 'ikigai.pdf__chunk_21', 'text': 'o the group. This\npayment allows them to participate in meetings, dinners, games of go and shogi\n(Japanese chess), or whatever hobby they have in common.\nThe funds collected by the group are used for activities, but if there is money\nleft over, one member (decided on a rotating basis) receives a set amount from\nthe surplus. In this way, being part of a moai helps maintain emotional and\nfinancial stability. If a member of a moai is in financial trouble, he or she can get\nan advance from the group’s savings. While the details of each moai’s accounting\npractices vary according to the group and its economic means, the feeling of\nbelonging and support gives the individual a sense of security and helps increase\nlife expectancy.\n• • •\nFOLLOWING THIS BRIEF introduction to the topics covered in this book, we look at\na few causes of premature aging in modern life, and then explore different\nfactors related to ikigai.\nII\nANTIAGING SECRETS\nLittle things that add up to a long\nand happy life\nAging’s', 'vector_score': 0.388457298, 'hybrid_score': 0.2913429735, 'rerank_score': 0.6934170722961426}]

top_candidates: [('igai: A mysterious word\nI. Ikigai\nThe art of staying young while growing old\nII. Antiaging Secrets\nLittle things that add up to a long and happy life\nIII. From Logotherapy to Ikigai\nHow to live longer and better by finding your purpose\nIV. Find Flow in Everything You Do\nHow to turn work and free time into spaces for growth\nV. Masters of Longevity\nWords of wisdom from the longest-living people in the world\nVI. Lessons from Japan’s Centenarians\nTraditions and proverbs for happiness and longevity\nVII. The Ikigai Diet\nWhat the world’s longest-living people eat and drink\nVIII. Gentle Movements, Longer Life\nExercises from the East that promote health and longevity\nIX. Resilience and Wabi-sabi\nHow to face life’s challenges without letting stress and worry age you\nEpilogue\nIkigai: The art of living\nNotes\nSuggestions for further reading\nAbout the Authors\nPROLOGUE\nIkigai: A mysterious word\nTHIS BOOK FIRST came into being on a rainy night in Tokyo, when its authors sat\ndown together for the first', 6.290822505950928), ('GARCÍA AND FRANCESC M\nIRALLES\nI\nIKIGAI\nThe art of staying young while\ngrowing old\nWhat is your reason for being?\nAccording to the Japanese, everyone has an ikigai—what a French philosopher\nmight call a raison d’être. Some people have found their ikigai, while others are\nstill looking, though they carry it within them.\nOur ikigai is hidden deep inside each of us, and finding it requires a patient\nsearch. According to those born on Okinawa, the island with the most\ncentenarians in the world, our ikigai is the reason we get up in the morning.\nWhatever you do, don’t retire!\nHaving a clearly defined ikigai brings satisfaction, happiness, and meaning to our\nlives. The purpose of this book is to help you find yours, and to share insights\nfrom Japanese philosophy on the lasting health of body, mind, and spirit.\nOne surprising thing you notice, living in Japan, is how active people remain\nafter they retire. In fact, many Japanese people never really retire—they keep\ndoing what they love for as', 6.289592266082764), ('sexual hormones until much later\nin life.\nThe rate of dementia is well below the global average.\nThe Characters Behind Ikigai\nIn Japanese, ikigai is written as 生き甲斐, combining 生き, which means\n“life,” with 甲斐, which means “to be worthwhile.” 甲斐 can be broken\ndown into the characters 甲, which means “armor,” “number one,” and “to\nbe the first” (to head into battle, taking initiative as a leader), and 斐,\nwhich means “beautiful” or “elegant.”\nThough we will consider each of these findings over the course of the book,\nresearch clearly indicates that the Okinawans’ focus on ikigai gives a sense of\npurpose to each and every day and plays an important role in their health and\nlongevity.\nThe five Blue Zones\nOkinawa holds first place among the world’s Blue Zones. In Okinawa, women in\nparticular live longer and have fewer diseases than anywhere else in the world.\nThe five regions identified and analyzed by Dan Buettner in his book The Blue\nZones are:\n1. Okinawa, Japan (especially the northern par', 5.818521022796631)]


prompt: [You are an AI assistant. Use ONLY the provided context snippets below to answer the user's question.
If the information is not present in the context, say "I couldn't find relevant information."

Context:
[1] (score: 6.291)
igai: A mysterious word
I. Ikigai
The art of staying young while growing old
II. Antiaging Secrets
Little things that add up to a long and happy life
III. From Logotherapy to Ikigai
How to live longer and better by finding your purpose
IV. Find Flow in Everything You Do
How to turn work and free time into spaces for growth
V. Masters of Longevity
Words of wisdom from the longest-living people in the world
VI. Lessons from Japan’s Centenarians
Traditions and proverbs for happiness and longevity
VII. The Ikigai Diet
What the world’s longest-living people eat and drink
VIII. Gentle Movements, Longer Life
Exercises from the East that promote health and longevity
IX. Resilience and Wabi-sabi
How to face life’s challenges without letting stress and worry age you
Epilogue
Ikigai: The art of living
Notes
Suggestions for further reading
About the Authors
PROLOGUE
Ikigai: A mysterious word
THIS BOOK FIRST came into being on a rainy night in Tokyo, when its authors sat
down together for the first

[2] (score: 6.290)
GARCÍA AND FRANCESC M
IRALLES
I
IKIGAI
The art of staying young while
growing old
What is your reason for being?
According to the Japanese, everyone has an ikigai—what a French philosopher
might call a raison d’être. Some people have found their ikigai, while others are
still looking, though they carry it within them.
Our ikigai is hidden deep inside each of us, and finding it requires a patient
search. According to those born on Okinawa, the island with the most
centenarians in the world, our ikigai is the reason we get up in the morning.
Whatever you do, don’t retire!
Having a clearly defined ikigai brings satisfaction, happiness, and meaning to our
lives. The purpose of this book is to help you find yours, and to share insights
from Japanese philosophy on the lasting health of body, mind, and spirit.
One surprising thing you notice, living in Japan, is how active people remain
after they retire. In fact, many Japanese people never really retire—they keep
doing what they love for as

[3] (score: 5.819)
sexual hormones until much later
in life.
The rate of dementia is well below the global average.
The Characters Behind Ikigai
In Japanese, ikigai is written as 生き甲斐, combining 生き, which means
“life,” with 甲斐, which means “to be worthwhile.” 甲斐 can be broken
down into the characters 甲, which means “armor,” “number one,” and “to
be the first” (to head into battle, taking initiative as a leader), and 斐,
which means “beautiful” or “elegant.”
Though we will consider each of these findings over the course of the book,
research clearly indicates that the Okinawans’ focus on ikigai gives a sense of
purpose to each and every day and plays an important role in their health and
longevity.
The five Blue Zones
Okinawa holds first place among the world’s Blue Zones. In Okinawa, women in
particular live longer and have fewer diseases than anywhere else in the world.
The five regions identified and analyzed by Dan Buettner in his book The Blue
Zones are:
1. Okinawa, Japan (especially the northern par

Question: what ikigai

Answer concisely, and include citations like [1], [2] referring to the context snippets above when you use them.]

respose_json: {'model': 'gpt-oss:20b', 'created_at': '2025-11-19T10:54:32.406418125Z', 'message': {'role': 'assistant', 'content': 'Ikigai is the Japanese concept of “the reason for being” – the purpose or passion that makes life feel worthwhile and motivates one to get up each day. It combines the Japanese words 生き\u202f“life” and 甲斐\u202f“to be worthwhile” [3], and is often described as a personal raison d’être that brings satisfaction, happiness, and meaning to life [2].', 'thinking': 'The user asks: "Question: what ikigai" They want the definition of ikigai. The context includes some definitions: in snippet [2], "What is your reason for being? According to the Japanese, everyone has an ikigai—what a French philosopher might call a raison d’être." Also snippet [3] includes explanation: "In Japanese, ikigai is written as 生き甲斐, combining 生き, which means \'life,\' with 甲斐, which means \'to be worthwhile.\'" So answer concisely: Ikigai is a Japanese concept meaning the reason for being, a sense of purpose that makes life worthwhile, the reason one gets up in the morning. Provide citations. So answer with citations [2] and [3]. Let\'s respond.'}, 'done': True, 'done_reason': 'stop', 'total_duration': 45304966873, 'load_duration': 5660748434, 'prompt_eval_count': 905, 'prompt_eval_duration': 16582426241, 'eval_count': 254, 'eval_duration': 22706342677}