import player

if __name__ == "__main__":
    julio = player.Player('omar')
    julio.wallet = 0 
    julio.xx=10
    julio.yy=12
    julio.player_to_yaml(julio.makedict())
    print('hello world!!')  
  