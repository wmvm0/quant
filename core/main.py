import json
import os
import js2py

import requests

from src.quant.ji_jin.public.ji_jin import JiJin
import pymysql as db
from config import DB_CONFIG

env = os.getenv('%u4FE1%u8BDA%u4E2D%u8BC1800%u6709%u8272%u6307%u6570%28LOF%29A@%23%24165520')

cookies = {
    'qgqp_b_id': 'c0cd9e345ab6900477bbbb7588e1bae6',
    'intellpositionL': '1215.35px',
    'intellpositionT': '455px',
    'em_hq_fls': 'js',
    'HAList': 'f-0-000001-%u4E0A%u8BC1%u6307%u6570%2Cf-0-000016-%u4E0A%u8BC150%2Cf-0-000011-%u57FA%u91D1%u6307%u6570',
    'searchbar_code': '005827_110003',
    'EMFUND1': 'null',
    'EMFUND2': 'null',
    'EMFUND3': 'null',
    'EMFUND4': 'null',
    'EMFUND5': 'null',
    'EMFUND6': 'null',
    'EMFUND7': 'null',
    'st_si': '91892747616226',
    'st_asi': 'delete',
    'ASP.NET_SessionId': '35wbgnisgwbr4njsbrjcbzp4',
    '_adsame_fullscreen_18503': '1',
    'EMFUND0': 'null',
    'EMFUND8': '10-14%2014%3A01%3A54@%23%24%u6613%u65B9%u8FBE%u4E0A%u8BC150%u589E%u5F3AA@%23%24110003',
    'EMFUND9': f"10-16 11:21:00@#{env}",
    '_adsame_fullscreen_16928': '1',
    'st_pvi': '14676736433559',
    'st_sp': '2021-04-29%2022%3A15%3A07',
    'st_inirUrl': 'https%3A%2F%2Fcn.bing.com%2F',
    'st_sn': '22',
    'st_psi': '20211016113207520-112200304021-3205213288',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://fund.eastmoney.com/data/fundranking.html',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
}

stringify_js = """
function stringify(source) {
  // source: var rankData = {}
  eval(source)
  return JSON.stringify(rankData)
}
"""
stringify = js2py.eval_js(stringify_js)


def get_rows_data(page: int, size: int):
    print(str(page) + ' --> ' + str(size))
    params = (
        ('op', 'ph'),
        ('dt', 'kf'),
        ('ft', 'zs'),  # 猜测是当前基金的类型，这里是 指数基金
        ('rs', ''),
        ('gs', '0'),
        ('sc', '6yzf'),
        ('st', 'desc'),
        ('sd', '2020-10-16'),  # start_date
        ('ed', '2021-10-16'),  # end_date
        ('qdii', '|'),
        ('tabSubtype', ',,,,,'),
        ('pi', '' + str(page)),  # page_index 当前第几页
        ('pn', '' + str(size)),  # page_num  每页数量
        ('dx', '1'),
        ('v', '0.697360301890213'),
    )
    response = requests.get('https://fund.eastmoney.com/data/rankhandler.aspx', headers=headers, params=params,
                            cookies=cookies)
    ret = stringify(response.text)
    json_str = json.loads(ret)
    data = json_str['datas']
    stat_data = {
        "allRecords": 0,  # 当前基金的总记录数量
        "pageIndex": 0,  # 当前基金的在第几页
        "pageNum": 0,  # 当前基金所在页数
        "allPages": 0,  # 当前基金总页数
        "allNum": 0,  # 所有基金数量
        "gpNum": 0,  # 股票型基金
        "hhNum": 0,  # 混合型基金
        "zqNum": 0,  # 债券型基金
        "zsNum": 0,  # 指数型基金
        "bbNum": 0,
        "qdiiNum": 0,  # QDII型基金
        "etfNum": 0,
        "lofNum": 0,
        "fofNum": 0
    }
    key_list = stat_data.keys()
    for key in key_list:
        stat_data[key] = json_str[key]
    rows = []
    for item in data:
        info_list = item.split(',')
        row_data = {
            'code': info_list[0],
            'name': info_list[1],
            'date': info_list[3],
            'unit_net_value': parse_str_to_float(info_list[4]),
            'acc_net_value': parse_str_to_float(info_list[5]),
            'day_incr_rate': parse_str_to_float(info_list[6]),
            'one_week_incr_rate': parse_str_to_float(info_list[7]),
            'one_month_incr_rate': parse_str_to_float(info_list[8]),
            'three_month_incr_rate': parse_str_to_float(info_list[9]),
            'six_month_incr_rate': parse_str_to_float(info_list[10]),
            'one_year_incr_rate': parse_str_to_float(info_list[11]),
            'two_year_incr_rate': parse_str_to_float(info_list[12]),
            'three_year_incr_rate': parse_str_to_float(info_list[13]),
            'this_year_incr_rate': parse_str_to_float(info_list[14]),
            'all_incr_rate': parse_str_to_float(info_list[15]),
            'service_charge': parse_str_to_float(info_list[20].replace('%', '')),
        }
        rows.append(row_data)

    return rows


# 使用实体类存储 json
def get_rows_data_v2(page: int, size: int) -> [JiJin]:
    print(str(page) + ' --> ' + str(size))
    params = (
        # op ph，基金排行的意思
        ('op', 'ph'),
        # dt kf 开发基金的用车
        ('dt', 'kf'),
        #  指数：zs
        # ft filter_type 过滤类型
        ('ft', 'all'),
        ('rs', ''),
        ('gs', '0'),
        ('sc', '6yzf'),
        ('st', 'desc'),
        ('sd', '2005-10-16'),  # start_date
        ('ed', '2021-10-16'),  # end_date
        ('qdii', '|'),
        ('tabSubtype', ',,,,,'),
        ('pi', '' + str(page)),  # page_index 当前第几页
        ('pn', '' + str(size)),  # page_num  每页数量
        ('dx', '1'),
        ('v', '0.697360301890213'),
    )
    response = requests.get('https://fund.eastmoney.com/data/rankhandler.aspx', headers=headers, params=params,
                            cookies=cookies)
    ret = stringify(response.text)
    json_str = json.loads(ret)
    data = json_str['datas']
    stat_data = {
        "allRecords": 0,  # 当前基金的总记录数量
        "pageIndex": 0,  # 当前基金的在第几页
        "pageNum": 0,  # 当前基金所在页数
        "allPages": 0,  # 当前基金总页数
        "allNum": 0,  # 所有基金数量
        "gpNum": 0,  # 股票型基金
        "hhNum": 0,  # 混合型基金
        "zqNum": 0,  # 债券型基金
        "zsNum": 0,  # 指数型基金
        "bbNum": 0,
        "qdiiNum": 0,  # QDII型基金
        "etfNum": 0,
        "lofNum": 0,
        "fofNum": 0
    }
    key_list = stat_data.keys()
    for key in key_list:
        stat_data[key] = json_str[key]
    rows = []
    for item in data:
        info_list = item.split(',')
        ji_jin = JiJin()
        ji_jin.code = info_list[0]
        ji_jin.name = info_list[1]
        ji_jin.date = info_list[3]
        ji_jin.unit_net_value = parse_str_to_float(info_list[4])
        ji_jin.acc_net_value = parse_str_to_float(info_list[5])
        ji_jin.day_incr_rate = parse_str_to_float(info_list[6])
        ji_jin.one_week_incr_rate = parse_str_to_float(info_list[7])
        ji_jin.one_month_incr_rate = parse_str_to_float(info_list[8])
        ji_jin.three_month_incr_rate = parse_str_to_float(info_list[9])
        ji_jin.six_month_incr_rate = parse_str_to_float(info_list[10])
        ji_jin.one_year_incr_rate = parse_str_to_float(info_list[11])
        ji_jin.two_year_incr_rate = parse_str_to_float(info_list[12])
        ji_jin.three_year_incr_rate = parse_str_to_float(info_list[13])
        ji_jin.this_year_incr_rate = parse_str_to_float(info_list[14])
        ji_jin.all_incr_rate = parse_str_to_float(info_list[15])
        ji_jin.service_charge = parse_str_to_float(info_list[20].replace('%', ''))
        rows.append(ji_jin)

    return rows


def parse_str_to_float(origin: str) -> float:
    if origin is None or origin == '':
        return 0
    return float(origin)


def get_total_data(_type: str) -> int:
    page = 1
    size = 50
    params = (
        ('op', 'ph'),
        ('dt', 'kf'),
        # filter_type
        # all 全部
        # gp 股票
        ('ft', _type),  # 猜测是当前基金的类型，这里是 指数基金
        ('rs', ''),
        ('gs', '0'),
        ('sc', '6yzf'),
        ('st', 'desc'),
        ('sd', '2005-10-16'),  # start_date
        ('ed', '2021-10-16'),  # end_date
        ('qdii', '|'),
        ('tabSubtype', ',,,,,'),
        ('pi', '' + str(page)),  # page_index 当前第几页
        ('pn', '' + str(size)),  # page_num  每页数量
        ('dx', '1'),
        ('v', '0.697360301890213'),
    )
    response = requests.get('https://fund.eastmoney.com/data/rankhandler.aspx', headers=headers, params=params,
                            cookies=cookies)
    ret = stringify(response.text)
    json_str = json.loads(ret)
    data = json_str['datas']
    stat_data = {
        "allRecords": 0,  # 当前基金的总记录数量
        "pageIndex": 0,  # 当前基金的在第几页
        "pageNum": 0,  # 当前基金所在页数
        "allPages": 0,  # 当前基金总页数
        "allNum": 0,  # 所有基金数量
        "gpNum": 0,  # 股票型基金
        "hhNum": 0,  # 混合型基金
        "zqNum": 0,  # 债券型基金
        "zsNum": 0,  # 指数型基金
        "bbNum": 0,
        "qdiiNum": 0,  # QDII型基金
        "etfNum": 0,
        "lofNum": 0,
        "fofNum": 0
    }
    key_list = stat_data.keys()
    for key in key_list:
        stat_data[key] = json_str[key]
    return stat_data['allPages']


def save_data(connection, param):
    cursor = connection.cursor()
    sql_str = 'insert into ji_jin (' \
              'code,name,date,' \
              'unit_net_value,acc_net_value,' \
              'day_incr_rate,one_week_incr_rate,one_month_incr_rate,three_month_incr_rate,six_month_incr_rate,' \
              'one_year_incr_rate,two_year_incr_rate,three_year_incr_rate,this_year_incr_rate,all_incr_rate' \
              ') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    print(sql_str)
    try:
        cursor.execute(sql_str, param)
    except Exception:
        print(env)
    finally:
        cursor.close()
        connection.commit()


def get_connection():
    connection = db.connect(host=DB_CONFIG['host'], user=DB_CONFIG['user'], password=DB_CONFIG['password'],
                            db=DB_CONFIG['db'],
                            connect_timeout=10000, )
    return connection


def get_data():
    connection = get_connection()
    total_page = get_total_data('all')
    print(total_page)
    for i in range(total_page):
        rows = get_rows_data_v2(i + 1, 50)
        for row_data in rows:
            row = [
                row_data.code,
                row_data.name,
                row_data.date,
                row_data.unit_net_value,
                row_data.acc_net_value,
                row_data.day_incr_rate,
                row_data.one_week_incr_rate,
                row_data.one_month_incr_rate,
                row_data.three_month_incr_rate,
                row_data.six_month_incr_rate,
                row_data.one_year_incr_rate,
                row_data.two_year_incr_rate,
                row_data.three_year_incr_rate,
                row_data.this_year_incr_rate,
                row_data.all_incr_rate,
            ]
            save_data(connection, row)
    connection.close()


if __name__ == '__main__':
    get_data()
