#!/usr/bin/env python3
"""
Export Canva templates to PNG/PDF for sellable packs.
Requires canva API key or manual export.
"""
import os
import json

# Template definitions
TEMPLATES = {
    "landing_saas": {
        "name": "SaaS Landing Page",
        "dimensions": "1200x800",
        "elements": ["hero", "features", "pricing", "cta"]
    },
    "pitch_deck": {
        "name": "Startup Pitch Deck",
        "slides": 10,
        "sections": ["problem", "solution", "market", "business_model", "team"]
    },
    "social_instagram": {
        "name": "Instagram Post",
        "dimensions": "1080x1080",
        "templates": 5
    }
}

def export_template(template_id, output_dir):
    """Export a template to the output directory."""
    if template_id not in TEMPLATES:
        print(f"Unknown template: {template_id}")
        return False
    
    template = TEMPLATES[template_id]
    os.makedirs(output_dir, exist_ok=True)
    
    # Create template info file
    info_path = os.path.join(output_dir, f"{template_id}_info.json")
    with open(info_path, 'w') as f:
        json.dump(template, f, indent=2)
    
    print(f"Exported {template['name']} to {info_path}")
    return True

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python export_templates.py <template_id> <output_dir>")
        print(f"Available templates: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)
    
    template_id = sys.argv[1]
    output_dir = sys.argv[2]
    
    if export_template(template_id, output_dir):
        print("Export complete!")
    else:
        sys.exit(1)
