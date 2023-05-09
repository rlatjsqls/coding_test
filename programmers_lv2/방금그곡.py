def func(song):
    result = []
    for i in song:
        if i == '#':
            result.append(result.pop().lower())
        else:
            result.append(i)
    return ''.join(result)

def solution(m, musicinfos):
    answer = ''
    avail_music = []
    
    for song_order, i in enumerate(musicinfos):
        splited_data = i.split(',')
        
        t = (int(splited_data[1][0:2]) - int(splited_data[0][0:2])) * 60 + (int(splited_data[1][3:]) - int(splited_data[0][3:]))    #음악이 플레이된 시간을 계산
        time = t        #나중에 배열에 플레이된 시간을 넣기위해서 t를 복사
        play = ''       #플레이된 시간동안 나온 멜로디
        idx = 0         #음악의 인덱스용
        song = func(splited_data[3])    # #이 들어있는것을 소문자로 바꿔주는 함수
        size = len(song)                # 인덱스가 벗어나는 경우를 방지하기 위한 최대 길이
        
        #플레이 된 시간동안 나온 멜로디를 play에 저장
        while t:
            if idx == size:
                idx = 0
            play += song[idx]
            t -= 1
            idx += 1
            
        #m이 play안에 있다면 가능한 목록에 넣어준다.
        if func(m) in play:
            avail_music.append([time, splited_data[2], song_order])
            
    if avail_music:
        #플레이된 시간이 길고, 음악이 먼저 입력된 순서로 정렬 후 맨 첫번째 값의 노래제목 리턴
        return sorted(avail_music, key = lambda x : (-x[0],x[2]))[0][1]
    else:
        return "(None)"