#!/bin/dash

# 每一个arg都是一个目录
for dir in "$@"
do
  # 得到专辑名
  album=$(echo "$dir" | cut -d'/' -f2)
  # 年份
  year=$(echo "$album" | cut -d',' -f2 | cut -d' ' -f2)

  # 进入到目录 形式为 music/newdirc
  cd "$dir" || exit
  # 遍历当前目录下每一个music
  for music in *
  do  
    track=$(echo "$music" | cut -d'/' -f3 | cut -d' ' -f1)
    #                                       这里的sed是将最前面的空格以及最后面的空格删除
    title=$(echo "$music" | cut -d'-' -f2 | sed "s/^ //g;s/ $//g")
    #music/Triple J Hottest 100, 1995/11 - Lump - Presidents of the U.S.A..mp3
    # 因为会出现类似于U.S.A..mp3 的情况 所以我们使用sed "s/.mp3$//g" 而不是cut -d'.'
    artist=$(echo "$music" | cut -d'-' -f3 | sed "s/.mp3$//g" | sed "s/^ //g;s/ $//g")
    # set the id3
    id3 -t "$title" -T "$track" -a "$artist" -A "$album" -y "$year" "$music" > /dev/null
  done
  # 退出到上上级目录 因为之前进了两级
  cd ../..
done


主要思路：

1. 遍历每一个arg（也就是目录）
2.得到专辑名字 和年份
3.进入到目录里，遍历每一个文件（music）
  a.得到track， title， artist
  b.set id3
4. 退出到之前的文件夹，继续step1的循环