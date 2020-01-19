from django.shortcuts import render
import requests
from key.lolkey import *
from app.models import *


def Search(request):       #전적갱신을 눌렀을 때 보기.
    name=request.GET.get('name')
    if request.method=="GET":
        url="https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +name
        parmas={'api_key':api_key}
        res=requests.get(url,params=parmas)
        print('awefawefawef',res)

        sum_result={}
        team_tier = {}
        solo_tier = {}
        store_list=[]

        if res.status_code==requests.codes.ok:
            summoner_result=res.json()             #json = javascript를 python 으로 받는거
            if summoner_result:
                sum_result['name']=summoner_result['name']
                sum_result['level']=summoner_result['summonerLevel']
                sum_result['id']=summoner_result['id']

                tier_url="https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" +sum_result['id']
                tier_info=requests.get(tier_url,params=parmas)
                tier_info=tier_info.json()

                if len(tier_info)==1:
                    tier_info = tier_info.pop()
                    if tier_info['queueType']=='RANKED_SOLO_5x5': #솔로랭크
                        solo_tier['rank_type'] = '팀랭크 5:5'
                        solo_tier['tier'] = tier_info['tier']
                        solo_tier['rank'] = tier_info['rank']
                        solo_tier['points'] = tier_info['leaguePoints']
                        solo_tier['wins'] = tier_info['wins']
                        solo_tier['losses'] = tier_info['losses']
                        qs = loldb(name=sum_result['name'],solo_tier=solo_tier['tier'],
                                   solo_rank=solo_tier['rank'], solo_point=solo_tier['points'],
                                   solo_win=solo_tier['wins'],
                                   solo_loss=solo_tier['losses'])
                        qs.save()

                    else:  # 팀랭크인 경우
                        team_tier['rank_type'] = '자유랭크 5:5'
                        team_tier['tier'] = tier_info['tier']
                        team_tier['rank'] = tier_info['rank']
                        team_tier['points'] = tier_info['leaguePoints']
                        team_tier['wins'] = tier_info['wins']
                        team_tier['losses'] = tier_info['losses']
                        qs = loldb(name=sum_result['name'], team_tier=team_tier['tier'], team_rank=team_tier['rank'],
                                   team_point=team_tier['points'],team_win=team_tier['wins'], team_loss=team_tier['losses'],
                                  )
                        qs.save()

                if len(tier_info)==2:
                    print("tier_info : ",tier_info)
                    for item in tier_info:
                        store_list.append(item)
                    print("store_list : ",store_list)
                    solo_tier['rank_type'] = '솔로랭크 5:5'
                    solo_tier['tier'] = store_list[0]['tier']
                    solo_tier['rank'] = store_list[0]['rank']
                    solo_tier['points'] = store_list[0]['leaguePoints']
                    solo_tier['wins'] = store_list[0]['wins']
                    solo_tier['losses'] = store_list[0]['losses']

                    team_tier['rank_type'] = '자유랭크 5:5'
                    team_tier['tier'] = store_list[1]['tier']
                    team_tier['rank'] = store_list[1]['rank']
                    team_tier['points'] = store_list[1]['leaguePoints']
                    team_tier['wins'] = store_list[1]['wins']
                    team_tier['losses'] = store_list[1]['losses']
                    qs = loldb(name=sum_result['name'],team_tier=team_tier['tier'], team_rank=team_tier['rank'], team_point=team_tier['points'],
                               team_win=team_tier['wins'], team_loss=team_tier['losses'], solo_tier=solo_tier['tier'],
                               solo_rank=solo_tier['rank'], solo_point=solo_tier['points'], solo_win=solo_tier['wins'],
                               solo_loss=solo_tier['losses'])
                    qs.save()
    # name=request.GET.get('name')
    # db=loldb.objects.get(name=name)
    # return render(request,'view.html',{'db':db})
    return render(request,'view.html')

def view(request):         #db에서 불러와서 보기
    try:
        name = request.GET.get('name')
        db=loldb.objects.get(name=name)
        print(db)
        return render(request,'view.html', {'db': db})
    except:
        print("2")
        return render(request,'view.html')

def index(request):       #초기 구글같은 화면
    return render(request,'index.html')





#   r = requests.get(sohwan)
#   r.json()['id']
# Create your views here.
