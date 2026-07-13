import json
import random
import os
from datetime import datetime, timedelta

def generate_mock_data():
    resource_groups = [
        "rg-production-k8s",
        "rg-data-analytics",
        "rg-ai-ml-models",
        "rg-backend-services",
        "rg-frontend-apps",
        "rg-database-clusters"
    ]
    
    # Generate daily costs for the last 30 days
    today = datetime.now()
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(29, -1, -1)]
    
    daily_trends = []
    for d in dates:
        day_cost = { "date": d, "total": 0, "breakdown": {} }
        for rg in resource_groups:
            # Random cost between $50 and $500 per day
            cost = round(random.uniform(50.0, 500.0), 2)
            day_cost["breakdown"][rg] = cost
            day_cost["total"] += cost
        day_cost["total"] = round(day_cost["total"], 2)
        daily_trends.append(day_cost)
        
    # Generate total costs
    total_by_rg = {rg: 0 for rg in resource_groups}
    for day in daily_trends:
        for rg, cost in day["breakdown"].items():
            total_by_rg[rg] += cost
            
    for rg in total_by_rg:
        total_by_rg[rg] = round(total_by_rg[rg], 2)

    return {
        "last_updated": today.strftime("%Y-%m-%d %H:%M:%S"),
        "total_by_resource_group": total_by_rg,
        "daily_trends": daily_trends,
        "total_cost": round(sum(total_by_rg.values()), 2)
    }

def main():
    data = generate_mock_data()
    
    # Certificar que a pasta dashboard/data existe
    os.makedirs("dashboard/data", exist_ok=True)
    
    with open("dashboard/data/mock-data.json", "w") as f:
        json.dump(data, f, indent=4)
        
    print("Mock data generated successfully at dashboard/data/mock-data.json")

if __name__ == "__main__":
    main()
