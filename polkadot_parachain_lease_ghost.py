import requests, time

def lease_ghost():
    print("Polkadot — A Parachain Lease Just Vanished Into the Ghost Slot")
    seen = set()
    while True:
        r = requests.get("https://polkadot.api.subscan.io/api/scan/parachains/leases")
        for lease in r.json().get("data", {}).get("list", []):
            slot = lease["para_id"]
            if slot in seen: continue
            
            # Detect sudden lease drop / non-renewal of a live parachain
            if lease["lease_period_end"] - lease["current_period"] < 2:
                if int(lease["raised"]) > 5_000_000_000_000:  # >5M DOT ever raised
                    seen.add(slot)
                    print(f"A GHOST SLOT OPENED\n"
                          f"Parachain {slot} — {lease.get('name','Unknown')} — just lost its lease\n"
                          f"Raised in total: {int(lease['raised'])/1e10:,.1f} DOT\n"
                          f"Lease ends in {lease['lease_period_end'] - lease['current_period']} periods\n"
                          f"https://polkadot.subscan.io/parachain/{slot}\n"
                          f"→ A living world with thousands of users will be ejected into the void\n"
                          f"→ Crowdfund gods have spoken: your reality expires soon.\n"
                          f"→ In Polkadot, even universes have eviction notices.\n"
                          f"{'◉̷̴̷̴̷̴̷̴◉'*25}\n")
        time.sleep(12)

if __name__ == "__main__":
    lease_ghost()
