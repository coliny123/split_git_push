song = """When an eel grabs your arm,
And it causes great harm
That's - a moray!"""
song_list = song.split() #list와 split으로 단어 구분
print(song_list)
song_list[14] = song_list[14].title() #moray 위치 파악해서 리스트바꿈
song_string = " ".join(song_list) # string으로 다시 묶기
print(song_list)

print("""
hello
hi
my name is dohwan
ye
""")
print("i'm a boy")
print('i\'m a boy')
print('he said "hello"')
army ='안녕하세요' \
      '반가워요' \
      '잘있어요' \
      '다시만나요'
army2 ="안녕하세요\n반가워요\n잘있어요\n다시만나요"
army3 ="안녕하세요\t반가워요\t잘있어요\t다시만나요"

print(army)
print(army2)
print(army3)

start = "나 " * 4 + "\n"
middle = "헤이 " *3 + "\n"
end = "안녕"
print(start + middle + end)

#대화식 인터프리터가 교체 결과만출력하기 때문에 name에 저장된 값은 바뀌지 않는다.
name = "Henny"
name.replace("H", "P")
"P" + name[1:]

univ = "Inha University"
print(univ[5:])
print(univ[5:14]) #end-1까지 가져와서 짤림
print(univ[::2]) #0번부터 2번째씩
# 역방향 참조
print(univ[-10:])
print(univ[5:-6])
print(univ[-10:-6])

pokemons_list = ["피카츄", "꼬부기", "파이리", "이상해씨"]
pokemons_string = ", ".join(pokemons_list)
print(pokemons_list)
print(pokemons_string) #list에서 string으로 변경됨 "string".join(list)해서 정말 많이 쓰는 함수!

inha = "a duck goes into a sea"
print(inha.replace("a", "a nice"))
print(inha.replace("a ", "a nice"))

subject = "python, data structure, database"
print(subject.find("data"), subject.index("data"))
print(subject.find("inha")) #-1 던짐
print(subject.index("inha")) #오류던짐
print(subject.rfind("data"), subject.rindex("data")) #  문자열 끝에서 부분 문자열을 찾아서 오프셋을 얻음
