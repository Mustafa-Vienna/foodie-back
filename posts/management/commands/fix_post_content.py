from django.core.management.base import BaseCommand
from posts.models import Post
import re

class Command(BaseCommand):
  help = 'Parse and fix the content field of existing Post objects by splitting it into introduction, ingredients, steps, and conclusion.'

  def handle(self, *args, **options):
    self.stdout.write("Starting to fix Post content fields...")
    posts_updated = 0
    posts_skipped = 0

    for post in Post.objects.all():
      try:
        content = post.content
        if not isinstance(content, dict):
          self.stdout.write(f"Skipping Post ID {post.id}: Content is not a dictionary.")
          posts_skipped += 1
          continue

        # If ingredients, steps, or conclusion are already populated, skip this post
        if content.get("ingredients") or content.get("steps") or content.get("conclusion"):
          self.stdout.write(f"Skipping Post ID {post.id}: Content already has ingredients, steps, or conclusion.")
          posts_skipped += 1
          continue

        introduction_text = content.get("introduction", "")
        if not introduction_text:
          self.stdout.write(f"Skipping Post ID {post.id}: Introduction is empty.")
          posts_skipped += 1
          continue

        # Define the section headers
        sections = {
            "ingredients": r"Ingredients & Materials\r\n\r\n",
            "steps": r"Step-by-Step Cooking Process\r\n\r\n",
            "conclusion": r"Conclusion & Serving Suggestions\r\n\r\n"
        }

        # Initialize the new content structure
        new_content = {
            "introduction": "",
            "ingredients": [],
            "steps": [],
            "conclusion": ""
        }

        # Split the introduction text into sections
        # Find the start of each section
        ingredients_start = introduction_text.find(sections["ingredients"])
        steps_start = introduction_text.find(sections["steps"])
        conclusion_start = introduction_text.find(sections["conclusion"])

        # If any section is missing, handle accordingly
        if ingredients_start == -1:
          # No sections found; treat the entire text as introduction
          new_content["introduction"] = introduction_text.strip()
        else:
          # Extract introduction (before Ingredients & Materials)
          new_content["introduction"] = introduction_text[:ingredients_start].strip()

          # Extract ingredients (between Ingredients & Materials and Step-by-Step Cooking Process)
          if steps_start != -1:
            ingredients_text = introduction_text[ingredients_start + len(sections["ingredients"]):steps_start].strip()
            # Split ingredients by newlines and filter out empty lines
            new_content["ingredients"] = [
                item.strip() for item in ingredients_text.split("\r\n") if item.strip()
              ]
          else:
            # If steps are missing, ingredients go until conclusion or end
            end_of_ingredients = conclusion_start if conclusion_start != -1 else len(introduction_text)
            ingredients_text = introduction_text[ingredients_start + len(sections["ingredients"]):end_of_ingredients].strip()
            new_content["ingredients"] = [
              item.strip() for item in ingredients_text.split("\r\n") if item.strip()
            ]

          # Extract steps (between Step-by-Step Cooking Process and Conclusion & Serving Suggestions)
          if steps_start != -1:
            end_of_steps = conclusion_start if conclusion_start != -1 else len(introduction_text)
            steps_text = introduction_text[steps_start + len(sections["steps"]):end_of_steps].strip()
            new_content["steps"] = [
              item.strip() for item in steps_text.split("\r\n") if item.strip()
            ]

          # Extract conclusion (after Conclusion & Serving Suggestions)
          if conclusion_start != -1:
            conclusion_text = introduction_text[conclusion_start + len(sections["conclusion"]):].strip()
            new_content["conclusion"] = conclusion_text

        # Update the post with the new content structure
        post.content = new_content
        post.save()
        self.stdout.write(f"Updated Post ID {post.id} with new content structure.")
        posts_updated += 1

      except Exception as e:
        self.stdout.write(self.style.ERROR(f"Error updating Post ID {post.id}: {str(e)}"))
        posts_skipped += 1

    self.stdout.write(self.style.SUCCESS(f"Finished! Updated {posts_updated} posts, skipped {posts_skipped} posts."))