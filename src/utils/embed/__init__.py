import discord 

class EmbedMessage(discord.Embed):
    def __init__(self, title:str, color:int, author:str, description:str=None, timestamp:datetime=None, type:str ="rich") -> None:
        super().__init__(title=title,color=color,author=author,description=description,type=type, timestamp=timestamp)


    
    def field(self) -> None: 
        pass


    def footer(self) -> None:
        pass
    


    def create_rpg_table(self) -> None:
        pass


    def create_rpg_table_combat(self) -> None:
        pass 


    def finish_rpg_table(self) -> None:
        pass 

    def finish_rpg_table_combat(self) -> None:
        pass

    @classmethod
    def create_from_dict(self, dict: ) -> None:


    
