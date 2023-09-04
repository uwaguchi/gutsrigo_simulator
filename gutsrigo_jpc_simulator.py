import random

# 抽選
# 与えられたリストの中からランダムに1つ引いてその値を返す
def draw(draw_list):
    # 抽選！
    number = int(random.random() * len(draw_list))
    # 引いた数に対応するリストの値を返す
    return draw_list[number]

# 巻き取り長さ抽選
def drawing_makitori():
    # 値のリスト
    # 通常
    makitori_list = [1, 5, 5, 10, 10, 20] 
    # ハイビスカスがついた場合
    #makitori_list = [11, 5, 5, 10, 10, 20] 
    # 抽選
    return draw(makitori_list)

# テンションメーター抽選
def drawing_tension_meter():
    # 値のリスト
    tension_meter_list = [1, 1, 1, 1, 1, 1, 0, 0, 0, -1] 
    # 抽選
    return draw(tension_meter_list)

# JPC処理
def jackpot_challenge():
    # 各種初期値
    # テンションメータの位置
    # 0-5, 5になったら糸が切れて終了
    tension_meter_position = 2

    # 糸の長さ
    # 0-100, 0になったらJP獲得
    line_length = 100

    # 初期表示
    print("[開始]糸の長さ: " + str(line_length) + "m, テンション: " + str(tension_meter_position))
   
    # 抽選カウント
    count = 0
    # 終了条件を満たすまで無限ループ
    while True:
        # テンション抽選
        current_tension = drawing_tension_meter()
        # 巻き取り抽選
        current_makitori = drawing_makitori()
        # 抽選カウントインクリメント
        count += 1
        # 抽選結果表示
        print("[" + str(count) + "回目抽選]巻き取り: " + str(current_makitori) + ", テンション: " + str(current_tension))

        # 糸の長さ更新
        line_length -= current_makitori
        print("糸の長さ: " + str(line_length) + "m")

        # 糸の長さが０になったらJP獲得
        if line_length <= 0:
            print("JP獲得！！！！")
            # JPの場合はTrueを返す
            return True

        # テンションメータ位置更新
        tension_meter_position += current_tension
        print("テンションメーター位置: " + str(tension_meter_position))

        # テンションメータが5になったら糸がきれて終了
        if tension_meter_position >= 5:
            print("糸が切れた！終了。。。")
            # 失敗の場合はFalseを返す
            return False

# メイン処理
def main():
    # 成功カウント
    jpc_success = 0
    # 失敗カウント
    jpc_failure = 0
    
    # JPチャレンジ
    for i in range(1,1000001):
        print("<<<<" + str(i) + "回目 JPチャレンジ開始>>>>")
        if jackpot_challenge() == True:
            jpc_success += 1
        else:
            jpc_failure += 1
        print("")

    # 最終結果
    print("試行回数： " + str(jpc_success + jpc_failure))
    print("JP獲得回数： " + str(jpc_success))
    print("失敗回数： " + str(jpc_failure))
    print("JPC成功確率： " + str((float(jpc_success) / float((jpc_success + jpc_failure))) * 100.0) + "%")

if __name__ == "__main__":
    main()

