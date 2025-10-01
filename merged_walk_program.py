#!/usr/bin/env python3
"""
Merged walking program that combines balance adjustment and walking functionality.
Takes input for number of blocks to walk (0.6m per block).
Each iteration: adjusts left-right balance -> walks straight -> repeats
"""

import time

# Constants
BLOCK_DISTANCE = 0.6  # meters per block


def lock_axis_and_slide():
    """
    Adjusts left-right balance using axis locking mechanism.
    This function should implement the sliding adjustment from no_tited.py
    """
    print("🔒 Locking axis for balance adjustment...")
    time.sleep(0.1)
    
    # Implement axis locking mechanism here
    # This would involve:
    # - Reading IMU/gyroscope data
    # - Detecting tilt/imbalance
    # - Adjusting servo positions to compensate
    # - Using sliding mechanism to correct left-right balance
    
    print("⚖️  Adjusting left-right balance...")
    time.sleep(0.5)
    
    print("✓ Balance adjusted")


def walk_straight(distance):
    """
    Walks straight for the specified distance.
    This function should implement the walking mechanism from tong_yon_adeat.py
    """
    print(f"🚶 Walking straight for {distance}m...")
    
    # Implement walking mechanism here
    # This would involve:
    # - Calculating step parameters
    # - Executing gait sequence
    # - Monitoring distance traveled
    # - Adjusting for obstacles/drift
    
    # Simulate walking time (adjust based on actual robot speed)
    walk_time = distance / 0.3  # Assuming 0.3 m/s walking speed
    time.sleep(walk_time)
    
    print(f"✓ Completed {distance}m walk")


def main():
    """
    Main program loop:
    1. Get input for number of blocks
    2. For each block: adjust balance -> walk straight
    3. Repeat until complete
    """
    print("=" * 50)
    print("Robot Walking Program with Balance Adjustment")
    print("=" * 50)
    
    # Get user input
    try:
        num_blocks = int(input("\nEnter number of blocks to walk: "))
        if num_blocks <= 0:
            print("❌ Please enter a positive number")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a valid number")
        return
    
    total_distance = num_blocks * BLOCK_DISTANCE
    print(f"\nTarget: {num_blocks} blocks = {total_distance}m")
    print(f"Block size: {BLOCK_DISTANCE}m")
    print("\nStarting movement sequence...\n")
    
    # Main walking loop
    for block_num in range(1, num_blocks + 1):
        print(f"\n--- Block {block_num}/{num_blocks} ---")
        
        # Step 1: Adjust balance (from no_tited.py)
        lock_axis_and_slide()
        
        # Step 2: Walk straight (from tong_yon_adeat.py)
        walk_straight(BLOCK_DISTANCE)
        
        print(f"✓ Completed block {block_num}")
        
        # Small delay between blocks
        time.sleep(0.2)
    
    print("\n" + "=" * 50)
    print(f"✓ Successfully completed all {num_blocks} blocks!")
    print(f"✓ Total distance traveled: {total_distance}m")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
