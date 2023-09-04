import random

# 抽選
# 与えられたリストの中からランダムに1つ引いてその値を返す
def draw(draw_list):
    # 抽選！
    number = int(random.random() * len(draw_list))
    # 引いた数に対応するリストの値を返す
    return draw_list[number]

# 魚抽選
def drawing_fishtype():
    # 値のリスト
    # -1はサメ。70はタイ（ここを変えるとタイの配当が変わる）
    fishtype_list = [
            {'name': 'サメ', 'value': -1},
            {'name': 'ヒトデ', 'value': 10},
            {'name': 'エビ', 'value': 20},
            {'name': 'タコ', 'value': 30},
            {'name': 'カニ', 'value': 50},
            {'name': 'タイ', 'value': 300}
            ] 
    # 抽選
    return draw(fishtype_list)

# 釣り抽選
def drawing_fishing():
    # 値のリスト
    # 0は逃、1は釣り成功、2はボーナスプラスの釣り大成功
    fishing_list = [
            {'name': '逃', 'value': 0},
            {'name': '逃', 'value': 0},
            {'name': '逃', 'value': 0},
            {'name': '成功', 'value': 1},
            {'name': '成功', 'value': 1},
            {'name': '成功', 'value': 1},
            {'name': '成功', 'value': 1},
            {'name': '成功', 'value': 1},
            {'name': '成功', 'value': 1},
            {'name': '大成功(ボーナス)', 'value': 2}
            ] 
    # 抽選
    return draw(fishing_list)

# フィッシングrush処理
def fishing_rush():
    # 各種初期値
    # 獲得枚数
    get_count = 0

    # ボーナス
    bonus = 0

    # 初期表示
    print("[開始]獲得枚数: " + str(get_count) + " ボーナス: " + str(bonus))
   
    # 抽選カウント
    count = 0
    # 終了条件を満たすまで無限ループ
    while True:
        # 魚抽選
        current_fishtype = drawing_fishtype()
        # 釣り抽選
        current_fishing = drawing_fishing()
        # 抽選カウントインクリメント
        count += 1
        # 抽選結果表示
        print("[" + str(count) + "回目抽選]魚種類: " + current_fishtype['name'] + ", 釣り結果: " + current_fishing['name'])

        # 抽選結果による処理
        # 釣り成功
        if current_fishing['value'] == 1 or current_fishing['value'] == 2:
            # サメを釣った場合は終了
            if current_fishtype['value'] == -1:
                # 獲得0枚でサメを釣った場合は撃退
                if get_count == 0:
                    print("サメ撃退！継続")
                    continue
                else:
                    print("サメゲット、終了")
                    break

            # 通常
            if current_fishing['value'] == 1:
                # 魚の種類に応じた獲得枚数を追加
                get_count += current_fishtype['value']
                get_count += bonus
                print("釣り成功、" + str(current_fishtype['value']) + "枚+ボーナス" + str(bonus) + "枚獲得。合計" + str(get_count) + "枚。処理継続！")
            elif current_fishing['value'] == 2:
                # ボーナス追加
                bonus += 5
                get_count += current_fishtype['value']
                get_count += bonus
                print("釣り大成功、" + str(current_fishtype['value']) + "枚+ボーナス" + str(bonus) + "枚獲得。合計" + str(get_count) + "枚。処理継続！")
        elif current_fishing['value'] == 0:
            # 逃
            # ボーナス追加
            bonus += 1
            # サメの場合は回避
            if current_fishtype['value'] == -1:
                print("サメ回避、ボーナス+1で" + str(bonus) + "枚に。処理継続！")
            else:
                print("逃げられた。。でもボーナス+1で" + str(bonus) + "枚に。処理継続！")

    # 処理終了
    # 獲得枚数をリターン
    return get_count

# メイン処理
def main():
    # 獲得枚数履歴
    get_count_list = []

    # fishing rushチャレンジ
    for i in range(1,1000001):
        print("<<<<" + str(i) + "回目 fishing rush開始>>>>")
        # fishing rush を実行し、結果の獲得枚数を配列に入れる
        get_count = fishing_rush()
        print("獲得枚数： " + str(get_count) + "枚")
        get_count_list.append(get_count)

    # 集計
    # 平均 
    mean_get_count = sum(get_count_list) / len(get_count_list)
    # 最大
    max_get_count = max(get_count_list)
    
    print("試行回数： " + str(len(get_count_list)))
    print("平均獲得枚数： " + str(mean_get_count))
    print("最大獲得枚数： " + str(max_get_count))


if __name__ == "__main__":
    main()

