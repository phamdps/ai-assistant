"""
Local Qwen2-VL Vision & Weather Perception Module for Transportation Digital Twin
"""

import torch
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from PIL import Image

class TrafficVisionPerceiver:
    def __init__(self, model_id="Qwen/Qwen2.5-VL-7B-Instruct"):

        print(f"Loading local MLLM model: {model_id}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load processor with dynamic resolution parameters
        self.processor = AutoProcessor.from_pretrained(model_id, min_pixels=256*28*28, max_pixels=1024*28*28)
        
        # Load model with mixed precision or standard configuration depending on hardware
        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
            device_map="auto"
        )
        print("Qwen2-VL successfully loaded and ready for local inference.")

    def analyze_cctv_frame(self, image_path: str) -> str:
        """
        Parses a traffic CCTV snapshot to detect congestion, accidents, and weather conditions.
        """
        image = Image.open(image_path).convert("RGB")
        
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {
                        "type": "text", 
                        "text": "Analyze this traffic camera frame. Report vehicle density, any road blockages, and current weather/visibility conditions."
                    }
                ]
            }
        ]
        
        # Apply chat template and process inputs
        text_prompt = self.processor.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
        image_inputs, video_inputs = self.processor.image_processor([image], videos=None)
        
        inputs = self.processor(
            text=[text_prompt],
            images=image_inputs,
            padding=True,
            return_tensors="pt"
        ).to(self.device)
        
        # Generate analysis
        generated_ids = self.model.generate(**inputs, max_new_tokens=256)
        generated_ids_trimmed = [
            out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        output_text = self.processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )
        
        return output_text[0]

if __name__ == "__main__":
    # Example usage placeholder
    perceiver = TrafficVisionPerceiver()
    report = perceiver.analyze_cctv_frame("datasets/bjtt/sample_cctv.jpg")
    print(report)
    # pass