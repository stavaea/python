# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 15:18
# @Author : waxberry
# @File : 三、实际应用.py
# @Software : PyCharm

'''
接口协议如下（仅为演示需要，只展示部分内容）：
syntax = "proto3";

package sogou.parrot.inner.semantic.v1;
import "google/protobuf/duration.proto";
import "record.proto";
option go_package = "git.speech.sogou/semantic/v1;semantic";

service discourse_understand{
    rpc UnderstandFullText(stream UnderstandFullTextRequest) returns(stream UnderstandFullTextResponse);
}

message UnderstandFullTextRequest{
    repeated SubSentence sub_sentences = 1;
    repeated sogou.parrot.record.v1.NonSpeechSoundInfo sound_infos = 2;
    repeated sogou.parrot.record.v1.AIMark ai_marks = 3;
}

message UnderstandFullTextResponse{
        UnderstandFullTextResult result = 2;
}
'''
# 实现客户端的关键代码如下：

def gen_iterator(request):
    for r in [request]:
        yield r

def get_understand_full_textresponse(stub, ai_marks, sound_infos, sub_sentences):
    request = UnderstandFullTextRequest()
    request.sub_sentences.extend(sub_sentences)
    request.sound_infos.extend(sound_infos)
    request.ai_marks.extend(ai_marks)
    request_iter = gen_iterator(request)
    try:
        resps = stub.UnderstandFullText(request_iter)
        for resp in resps:
            resp_str = json.dumps(json.loads(MessageToJson(resp)),indent=4, ensure_ascii=False)
            print(resp_str)
    except Exception as e:
        print (e)

def run():
    ai_marks, sound_infos, sub_sentences = extract_data()
    with grpc.insecure_channel(sys.argv[2]) as channel:
        stub = discourse_understandStub(channel)
        print("-------------- UnderstandFullText --------------")
        get_understand_full_textresponse(stub, ai_marks, sound_infos, sub_sentences)

if __name__ == '__main__':
    run()