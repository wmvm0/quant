class JiJin:

    def __init__(self):
        self._code = None  # 基金代码
        self._name = None  # 基金名称
        self._date = None  # 日期，暂时没用
        self._unit_net_value = None  # 单位净值
        self._acc_net_value = None  # 累计净值
        self._day_incr_rate = None  # 日增长率
        self._one_week_incr_rate = None  # 近一周增长率
        self._one_month_incr_rate = None  # 近一月增长率
        self._three_month_incr_rate = None  # 近三月增长率
        self._six_month_incr_rate = None  # 近六月增长率
        self._one_year_incr_rate = None  # 近一年增长率
        self._two_year_incr_rate = None  # 近两年增长率
        self._three_year_incr_rate = None  # 近三年增长率
        self._this_year_incr_rate = None  # 今年以来增长率
        self._all_incr_rate = None  # 成立以来增长率
        self._service_charge = None  # 服务费占比

        self._feature_risk_grade_all = None  # 特色数据，占全部基金的风险等级排名
        self._feature_risk_grade_same = None  # 特色数据，占同类基金的风险等级排名

        self._feature_standard_deviation_1year = None  # 特色数据，基金风险指标 近1年标准差
        self._feature_sharpe_ratio_1year = None  # 特色数据，基金风险指标 近1年夏普比率
        self._feature_info_ratio_1year = None  # 特色数据，基金风险指标 近1年信息比率
        self._feature_standard_deviation_2year = None  # 特色数据，基金风险指标 近2年标准差
        self._feature_sharpe_ratio_2year = None  # 特色数据，基金风险指标 近2年夏普比率
        self._feature_info_ratio_2year = None  # 特色数据，基金风险指标 近2年信息比率
        self._feature_standard_deviation_3year = None  # 特色数据，基金风险指标 近2年标准差
        self._feature_sharpe_ratio_3year = None  # 特色数据，基金风险指标 近2年夏普比率
        self._feature_info_ratio_3year = None  # 特色数据，基金风险指标 近3年信息比率

        self._feature_trace_index = None  # 特色数据，基金指标 跟踪指数
        self._feature_trace_deviation = None  # 特色数据，基金指标 跟踪误差
        self._feature_trace_mean_deviation = None  # 特色数据，基金指标 同类平均跟踪误差

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def unit_net_value(self):
        return self._unit_net_value

    @unit_net_value.setter
    def unit_net_value(self, unit_net_value):
        self._unit_net_value = unit_net_value

    @property
    def acc_net_value(self):
        return self._acc_net_value

    @acc_net_value.setter
    def acc_net_value(self, acc_net_value):
        self._acc_net_value = acc_net_value

    @property
    def day_incr_rate(self):
        return self._day_incr_rate

    @day_incr_rate.setter
    def day_incr_rate(self, day_incr_rate):
        self._day_incr_rate = day_incr_rate

    @property
    def one_week_incr_rate(self):
        return self._one_week_incr_rate

    @one_week_incr_rate.setter
    def one_week_incr_rate(self, one_week_incr_rate):
        self._one_week_incr_rate = one_week_incr_rate

    @property
    def one_month_incr_rate(self):
        return self._one_month_incr_rate

    @one_month_incr_rate.setter
    def one_month_incr_rate(self, one_month_incr_rate):
        self._one_month_incr_rate = one_month_incr_rate

    @property
    def three_month_incr_rate(self):
        return self._three_month_incr_rate

    @three_month_incr_rate.setter
    def three_month_incr_rate(self, three_month_incr_rate):
        self._three_month_incr_rate = three_month_incr_rate

    @property
    def six_month_incr_rate(self):
        return self._six_month_incr_rate

    @six_month_incr_rate.setter
    def six_month_incr_rate(self, six_month_incr_rate):
        self._six_month_incr_rate = six_month_incr_rate

    @property
    def one_year_incr_rate(self):
        return self._one_year_incr_rate

    @one_year_incr_rate.setter
    def one_year_incr_rate(self, one_year_incr_rate):
        self._one_year_incr_rate = one_year_incr_rate

    @property
    def two_year_incr_rate(self):
        return self._two_year_incr_rate

    @two_year_incr_rate.setter
    def two_year_incr_rate(self, two_year_incr_rate):
        self._two_year_incr_rate = two_year_incr_rate

    @property
    def three_year_incr_rate(self):
        return self._three_year_incr_rate

    @three_year_incr_rate.setter
    def three_year_incr_rate(self, three_year_incr_rate):
        self._three_year_incr_rate = three_year_incr_rate

    @property
    def this_year_incr_rate(self):
        return self._this_year_incr_rate

    @this_year_incr_rate.setter
    def this_year_incr_rate(self, this_year_incr_rate):
        self._this_year_incr_rate = this_year_incr_rate

    @property
    def all_incr_rate(self):
        return self._all_incr_rate

    @all_incr_rate.setter
    def all_incr_rate(self, all_incr_rate):
        self._all_incr_rate = all_incr_rate

    @property
    def service_charge(self):
        return self._service_charge

    @service_charge.setter
    def service_charge(self, service_charge):
        self._service_charge = service_charge

    @property
    def feature_risk_grade_all(self):
        return self._feature_risk_grade_all

    @feature_risk_grade_all.setter
    def feature_risk_grade_all(self, feature_risk_grade_all):
        self._feature_risk_grade_all = feature_risk_grade_all

    @property
    def feature_risk_grade_same(self):
        return self._feature_risk_grade_same

    @feature_risk_grade_same.setter
    def feature_risk_grade_same(self, feature_risk_grade_same):
        self._feature_risk_grade_same = feature_risk_grade_same

    @property
    def feature_standard_deviation_1year(self):
        return self._feature_standard_deviation_1year

    @feature_standard_deviation_1year.setter
    def feature_standard_deviation_1year(self, feature_standard_deviation_1year):
        self._feature_standard_deviation_1year = feature_standard_deviation_1year

    @property
    def feature_sharpe_ratio_1year(self):
        return self._feature_sharpe_ratio_1year

    @feature_sharpe_ratio_1year.setter
    def feature_sharpe_ratio_1year(self, feature_sharpe_ratio_1year):
        self._feature_sharpe_ratio_1year = feature_sharpe_ratio_1year

    @property
    def feature_info_ratio_1year(self):
        return self._feature_info_ratio_1year

    @feature_info_ratio_1year.setter
    def feature_info_ratio_1year(self, feature_info_ratio_1year):
        self._feature_info_ratio_1year = feature_info_ratio_1year

    @property
    def feature_standard_deviation_2year(self):
        return self._feature_standard_deviation_2year

    @feature_standard_deviation_2year.setter
    def feature_standard_deviation_2year(self, feature_standard_deviation_2year):
        self._feature_standard_deviation_2year = feature_standard_deviation_2year

    @property
    def feature_sharpe_ratio_2year(self):
        return self._feature_sharpe_ratio_2year

    @feature_sharpe_ratio_2year.setter
    def feature_sharpe_ratio_2year(self, feature_sharpe_ratio_2year):
        self._feature_sharpe_ratio_2year = feature_sharpe_ratio_2year

    @property
    def feature_info_ratio_2year(self):
        return self._feature_info_ratio_2year

    @feature_info_ratio_2year.setter
    def feature_info_ratio_2year(self, feature_info_ratio_2year):
        self._feature_info_ratio_2year = feature_info_ratio_2year

    @property
    def feature_standard_deviation_3year(self):
        return self._feature_standard_deviation_3year

    @feature_standard_deviation_3year.setter
    def feature_standard_deviation_3year(self, feature_standard_deviation_3year):
        self._feature_standard_deviation_3year = feature_standard_deviation_3year

    @property
    def feature_sharpe_ratio_3year(self):
        return self._feature_sharpe_ratio_3year

    @feature_sharpe_ratio_3year.setter
    def feature_sharpe_ratio_3year(self, feature_sharpe_ratio_3year):
        self._feature_sharpe_ratio_3year = feature_sharpe_ratio_3year

    @property
    def feature_info_ratio_3year(self):
        return self._feature_info_ratio_3year

    @feature_info_ratio_3year.setter
    def feature_info_ratio_3year(self, feature_info_ratio_3year):
        self._feature_info_ratio_3year = feature_info_ratio_3year

    @property
    def feature_trace_index(self):
        return self._feature_trace_index

    @feature_trace_index.setter
    def feature_trace_index(self, feature_trace_index):
        self._feature_trace_index = feature_trace_index

    @property
    def feature_trace_deviation(self):
        return self._feature_trace_deviation

    @feature_trace_deviation.setter
    def feature_trace_deviation(self, feature_trace_deviation):
        self._feature_trace_deviation = feature_trace_deviation

    @property
    def feature_trace_mean_deviation(self):
        return self._feature_trace_mean_deviation

    @feature_trace_mean_deviation.setter
    def feature_trace_mean_deviation(self, feature_trace_mean_deviation):
        self._feature_trace_mean_deviation = feature_trace_mean_deviation
