
class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(singer) for singer in goods]


    def __map_to_trade(self, singer):
        if singer.create_datetime:
            time = singer.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=singer.user.nickname,
            time=time,
            id=singer.id
        )