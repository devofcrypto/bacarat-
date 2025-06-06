
import sys

print("🃏 Baccarat Safe Strategy Bot")
print("Only shows strong signals: Banker Bias, Streaks, Ping-Pong
")

history = []
balance = 100
unit = 5
wins = 0
losses = 0

def suggest_bet(history):
    if len(history) < 4:
        return "WAIT", "Not enough data"

    last4 = history[-4:]
    counts = {"B": history.count("B"), "P": history.count("P")}

    # Banker bias
    if counts["B"] >= len(history) * 0.7:
        return "BANKER", "Banker bias detected"

    # Streak
    if last4.count(last4[-1]) == 4:
        return last4[-1], "Streak detected"

    # Ping-pong
    if last4 == ["B", "P", "B", "P"] or last4 == ["P", "B", "P", "B"]:
        return "P" if last4[-1] == "B" else "B", "Ping-pong pattern"

    return "WAIT", "No strong pattern"

while True:
    print(f"\nCurrent Balance: ${balance} | Wins: {wins} | Losses: {losses}")
    print("History:", " ".join(history[-10:]))
    user_input = input("Enter last result (B/P/T) or Q to quit: ").upper()

    if user_input == "Q":
        print("Session ended.")
        break
    if user_input not in ["B", "P", "T"]:
        print("Invalid input. Use B, P, T, or Q.")
        continue

    history.append(user_input)
    signal, reason = suggest_bet(history)

    if signal in ["BANKER", "PLAYER", "B", "P"]:
        print(f"➡️ STRONG SIGNAL: BET {signal} 🔥 | Reason: {reason}")
        bet_result = input(f"Did you win the {signal} bet? (Y/N): ").upper()
        if bet_result == "Y":
            balance += unit
            wins += 1
        else:
            balance -= unit
            losses += 1
    else:
        print(f"⚠️ NO SAFE SIGNAL — {reason.upper()} — WAIT THIS ROUND")
