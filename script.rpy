﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# TODO: разные цвета персонажей
define e = Character('Евфрат', color="#c8ffc8")
define g = Character('Рыжий', color="#c8ffc8")
define d = Character('Тёмный', color="#c8ffc8")
define s = Character('Шелби', color="#c8ffc8")
define narrator = Character(None, what_italic=True)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Переменные для выборов
define choice_1 = []

# Игра начинается здесь:
label start:

    # Сцена 1. Экспозиция
    scene bg sleep with Dissolve(2.0)

    narrator "Просыпаться всегда было твоей слабой стороной."

    narrator "Ты вообще осознаешь, что весь тот абсурдный кошмар, который с тобой происходит, каждый раз начинается с твоего пробуждения?"

    narrator "Как клишейно."

    narrator "Слышишь, дети уже шумят снаружи? Тебе давно пора выходить из своей гримерки и являть свет… или тьму, тут уже отдам на твой откуп."

    narrator "Кто ты сегодня?"

    # {w} для появления следующего текста после клика мышкой
    narrator "Апофеоз Капельдинера? {w}Иммортальный Шталмейстер? {w}Бутафор Истории?"

    narrator "Или изволишь в кои-то веки явить свой лик публике со сцены впервые за несколько веков?"

    narrator "Впрочем, мне, по счету, клинически плевать."

    narrator "Вставай, Евфрат. {w}Вставай, Лорд Театра Времён."

    # TODO: *стук в дверь* (звук?)

    # Сцена 2. Злобное утро, дети
    scene bg morning with Dissolve(2.0)

    show e dissatisfied at right

    e "Хорош стучать, идиоты. {w}Я же вроде сплю."

    show e dissatisfied at center with MoveTransition(0.5)

    show g inspired at right with moveinright

    g "Доброе утро, дядя Евфрат!"

    g "Мы уже подготовили костюмы к сегодняшнему представлению! Хотите взглянуть?"

    show e at center with Dissolve(1.0)

    e "Увольте. {w}Ты выглядишь, как тот недоносок, что испортил мой отпуск в Париже лет этак двести назад… {w}… что, впрочем прекрасно подходит к сегодняшней постановке."

    show g dissatisfied at right with Dissolve(1.0)

    g "Вот именно! А этот идиот не желает совершенно наряжаться и все утро ходит в своей расчлененке!"

    show e at left with MoveTransition(0.5)

    show g dissatisfied at center with MoveTransition(0.5)

    show d tired at right with moveinright

    d "Я вижу мир на треть шире, чем ты и оттого прекрасно понимаю, что за псевдофилософской частью этого манифеста революционеров, который Евфрат нам подсунул, вообще ничего нет."

    show e smile at left with MoveTransition(0.5)

    d "Именно поэтому я надену костюм за час до представления."

    e "Принимается."

    g "Ну и ладно, носи свою расчлененку на груди… или что там у тебя?"

    show g inspired at center with Dissolve(1.0)

    g "Ой, дяденька Евфрат, а хотите, я вам фокус покажу? {w}Мне о нем Тёмный рассказал!"

    show e dissatisfied at left with Dissolve(1.0)

    e "Рыжий, ты же понимаешь, что я знаю вообще всё?"

    e "Мне твои фокусы до фени."

    g "Не верю!"

    g "Готов поспорить на желание, что вы секрет этого трюка не разгадаете!"

    e "Договорились."

    # Шокированное лицо Евфрата, широко открытые глаза.
    # TODO: скорее всего, можно сделать это не через scene, надо погуглить
    scene bg EBALO with Dissolve(2.0)
    
    $ renpy.pause()

    "Рыжий не пойми откуда сотворил себе сигарету и начал воодушевленно пытаться её закурить."

    "К удивлению Евфрата, последняя никак не хотела правильно вставать. Каждый раз, как Рыжий пытался поправить ситуацию, раковая палочка непослушно прыгала в его руках."

    "Через секунд сорок парень просто закинул цибарку к себе в рот и весело икнул."

    scene bg morning with Dissolve(2.0)

    show d tired at right with Dissolve(0.2)

    show g inspired at center with Dissolve(0.2)

    show e negative at left with Dissolve(0.2)

    e "Сдаюсь, у меня вообще нет ни одной идеи. {w}Давай сразу без лишней радости говори, чего хочешь."

    show g happy at center with Dissolve(1.0)

    g "Я хочу себе шаверму с курицей из той забегаловки в Канаде! {w}И обязательно с гранатом!"

    d "А мне бамбл из соседней кофейни… {w}пожалуйста."

    e "Ладно. {w}Катитесь уже, текст повторяйте. Скоро буду."

    # Сцена 3. Внешний мир
    scene bg outer_world with Dissolve(2.0)

    narrator "Евфрат, в принципе, редко бывал во внешнем мире. {w}В Канаду он так вообще попал чуть ли не впервые (если не считать Торонто в 1994, но об этом как-нибудь в другой раз)."

    narrator "На улицах какого-то достаточно урбанистичного города виднелись два смутно знакомых нашему имморталу места."

    narrator "Выбор был достаточно прост и тривиален: Евфрат мог пойти сначала в болотного цвета неброскую кофейню, а мог забежать в футуристично выглядящую шаверменную, на черных стенах которой ярко горела вывеска “У Шелби”."

    $ config.menu_include_disabled = True
    menu choice_1:
        "За кофе" if "coffee" not in choice_1:
            $ choice_1.append("coffee")
            jump coffee
            "тут что-то"

        "За шавермой" if "shawarma" not in choice_1:
            $ choice_1.append("shawarma")
            call shawarma
            "тут что-то"
    $ config.menu_include_disabled = False

    "тут чето ещё"

    return

label coffee:
    "тут рут кофи)"
    jump choice_1

label shawarma:
    e "Ладно, начнем с Рыжего. {w}Что он там хотел, шаверму с гранатом?"

    # Сцена 4. У Шелби
    scene shawarma

    narrator "В противовес классическим стереотипам о том, что заведения, где подают шаверму - грязные и неаккуратные, на внутреннее убранство “У Шелби” было приятно смотреть."

    narrator "Столы были натерты до блеска, из динамиков играли песни легенды черного шансона Игоря Демиурга, а за стойкой стоял улыбчивый и бородатый молодой человек."

    show s at right with Dissolve(1.0)

    s "Добрый день, молодой человек. {w}Что желаете?"
    jump choice_1
