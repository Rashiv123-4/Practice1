class Movie:
   
   def __init__(self, name, TicketNo, Price, SeatNo):
       self.name=name
       self.TicketNo=TicketNo
       self.Price=Price
       self.SeatNo=SeatNo


MT=Movie("LoveStory", 210, 400, "A12")
MT1=Movie("Fidaa", 310, 250, "B13")



print("{} is {} ticket no {} rs {}".format(MT.name, MT.TicketNo, MT.Price, MT.SeatNo))
print("{} is {} ticket no {} rs {}".format(MT1.name, MT1.TicketNo, MT1.Price, MT1.SeatNo))