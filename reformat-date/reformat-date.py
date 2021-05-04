class Solution:
    def reformatDate(self, date: str) -> str:
        mapMonth = {"Jan": "01", "Feb": "02","Mar": "03", "Apr":"04", "May":"05", "Jun":"06",                     "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        updateDate = ""
        if len(date) == 13:
            updateDate += date[-4:] + '-' + mapMonth[date[-8:-5]] + '-' + date[:2]
        else:
            updateDate += date[-4:] + '-' + mapMonth[date[-8:-5]] + '-0' + date[0]
        
        return updateDate
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         year = date[9:]
#         if 
#         mapValue = date[5:8]
#         monthNum = mapMonth[mapValue]
#         day = date[0:2]
        
#         return "".join((year + '-' + monthNum + '-' + day))
        