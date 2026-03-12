
import requests

class BestBrain:
    def __init__(self):
        self.free_model_url = "https://api.groq.com/openai/v1/chat/completions"
        self.api_key = ""

    def try_free_ai(self, prompt):
        try:
            r = requests.post(
                self.free_model_url,
                json={
                    "model": "llama3-8b-8192",
                    "messages": [{"role": "user", "content": prompt}]
                },
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=5
            )
            return r.json()["choices"][0]["message"]["content"]
        except:
            return None

    def fallback(self, prompt):
        return f"BestBrain received: {prompt} (fallback mode)"

    def process(self, prompt):
        result = self.try_free_ai(prompt)
        return result if result else self.fallback(prompt)
