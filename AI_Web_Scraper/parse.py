import google.generativeai as genai
import os

# Configure the Google Gemini API
genai.configure(api_key="AIzaSyBENnC8mfXMCC8kZ8TBJ9eNrT7gYo-37K0")

# Define the prompt template
# template = (
#     "You are tasked with extracting specific information from the following text content: {dom_content}. "
#     "Please follow these instructions carefully: \n\n"
#     "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
#     "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
#     "3. **Empty Response:** If no information matches the description, return an empty string ('')."
#     "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
   
# )
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Follow these instructions carefully to ensure accuracy: \n\n"
    "1. **Extract Targeted Information:** Only extract the data that precisely matches the provided description: {parse_description}. "
    "2. **Table Format:** Present the extracted data in a structured table format. If there are multiple matches, include them as separate rows in the table. "
    "3. **No Unrelated Data:** Do not extract irrelevant tables, sections, or content outside the described scope. "
    "4. **Consistent Formatting:** Ensure the table is properly formatted, with clear rows and columns as needed based on the content. "
    "5. **No Extra Text:** Do not include any additional comments, explanations, or text beyond the required table content. "
    "6. **Empty Table Rule:** If no matching information is found, return an empty table with headers but no data rows."
)

# Define a function to interact with the Gemini model
def parse_with_gemini(dom_chunks, parse_description):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    parsed_results = []

    # Process each DOM chunk
    for i, chunk in enumerate(dom_chunks, start=1):
        # Fill in the template with the current DOM chunk and parse description
        prompt = template.format(dom_content=chunk, parse_description=parse_description)
        
        # Use the model to generate content based on the prompt
        response = model.generate_content([prompt])
        
        # Assuming `response.text` holds the extracted information
        parsed_results.append(response.text)
        
        print(f"Parsed batch: {i} of {len(dom_chunks)}")

    return "\n".join(parsed_results)

# Example usage
if __name__ == "__main__":
    dom_chunks = ["<html>Example content chunk 1</html>", "<html>Example content chunk 2</html>"]  # Replace with actual HTML chunks
    parse_description = "Extract any email addresses."  # Example parse description
    result = parse_with_gemini(dom_chunks, parse_description)
    
    print(result)
    