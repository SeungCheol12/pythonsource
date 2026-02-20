from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr

# .env 파일 정보 가져오기
load_dotenv(find_dotenv())

client = OpenAI()


# 장르를 받은 후 장르 작가에게 알맞는 질문 8개 생성
# 장르 특징 5줄 정리
def interview_text(genre):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",  # system
                "content": "당신은 소설광이며 최고의 인터뷰어 입니다.",
            },
            {
                "role": "user",
                "content": f"""
                소설의 특정 장르를 입력 받으면 그 장르의 소설로써의 특징을 5줄 이내로 정리하고,
                그 장르의 소설을 쓰는 작가에게 알맞는 질문을 8개 생성해라.
                - 장르 : {genre}
             
                """,
            },
        ],
    )
    return response.output_text


demo = gr.Interface(
    fn=interview_text,
    inputs=[
        gr.Text(label="장르", placeholder="장르"),
    ],
    outputs=gr.Markdown(),
    title="작가의 인터뷰 질문 생성 프로그램 구현",
)

demo.launch()
