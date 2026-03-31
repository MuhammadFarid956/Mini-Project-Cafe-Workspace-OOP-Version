class BaseService:
    def _calculate_last_id(self, data_dict, prefix):
        last_id = 0
        for key in data_dict.keys():
            if key.startswith(prefix):
                try:
                    num = int(key.replace(prefix, ''))
                    if num > last_id:
                        last_id = num
                except ValueError:
                    pass
        return last_id
