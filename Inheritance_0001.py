class WebPush():
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.Platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_Push(self,name):
        return print(name + ": Push Gönderildi.")

class TriggerPush(WebPush):
    def __init__(self, trigger_page, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.trigger_page = trigger_page
        WebPush.__init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

class BulkPush(WebPush):
    def __init__(self, send_date, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.send_date = send_date
        WebPush.__init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

class SegmentPush(WebPush):
    def __init__(self, segment_name, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.segment_name = segment_name
        WebPush.__init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

class PriceAlertPush(WebPush):
    def __init__(self, price_info, discount_rate, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.price_info = price_info
        self.discount_rate = discount_rate
        WebPush.__init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

    def discountPrice(self, price_info, discount_rate):
        return (price_info * (discount_rate / 100))

class InstockPush(WebPush):
    def __init__(self, stock_info, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.stock_info = stock_info
        WebPush.__init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

    def stockUpdate(self):
        self.stock_info = not (bool(self.stock_info))
        return (self.stock_info)

web_push = WebPush("","","","","","","")
web_push.send_Push("web")

trigger_push = TriggerPush("","","","","","","","")
trigger_push.send_Push("trigger")

bulk_push = BulkPush("","","","","","","","")
bulk_push.send_Push("bulk")

segment_push = SegmentPush("","","","","","","","")
segment_push.send_Push("segment")

price_alert = PriceAlertPush(100,18,"","","","","","","")
price_alert.send_Push("price alert")
print("discount : {}".format(price_alert.discountPrice(100,18)))

instock_push = InstockPush(False,"","","","","","","")
instock_push.send_Push("instock")
print("Instock : {} ".format(instock_push.stockUpdate()))


