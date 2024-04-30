import google.generativeai as genai


model = genai.GenerativeModel('gemini-1.5-pro-latest')


response = model.generate_coontent{
    'tell me a story about a magic bagpack.'

    generation_config = genai.types.GenerationConfig{

        candidate_count = 1,

        # Stop generating if the output contains 'x'.
        stop_sequence = ['x'],

        # Maximum number of tokens to generate
        max_output_tokens = 8000,

        #temperature of the model. Higher values result in more creative but less coherent text.
        temperature = 1.0,

        # Top-p value. Higher values result in more likely but less diverse text.
        top_p = 0.95

    }
}