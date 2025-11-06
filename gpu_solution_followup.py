import heapq

class InsufficientCreditException(Exception):
    pass

class GPUSolution:
    def __init__(self):
        self.events = []

    def add_credit(self, grant_id: str, amount: int, timestamp: int, expire: int):
        self.events.append(('add', timestamp, amount, timestamp + expire, grant_id))
    
    def charge(self, amount: int, timestamp: int):
        self.events.append(('charge', timestamp, amount))

    def get_balance(self, timestamp: int) -> int:
        """Follow up 1: 负余额时抛异常"""
        balance = self._calculate_balance(timestamp)
        if balance < 0:
            raise InsufficientCreditException(f"Insufficient credit: balance is {balance}")
        return balance
    
    def get_balance_by_grant(self, grant_id: str, timestamp: int) -> int:
        """Follow up 2: 按grant_id查询余额"""
        valid_events = [e for e in self.events if e[1] <= timestamp]
        valid_events.sort(key=lambda x: x[1])
        
        active_grants = []
        
        for event in valid_events:
            if event[0] == 'add':
                _, ts, amount, expire_ts, gid = event
                if expire_ts > timestamp and gid == grant_id:
                    active_grants.append((expire_ts, amount, gid))
            elif event[0] == 'charge':
                _, ts, charge_amount = event
                remaining_charge = charge_amount
                
                # 优先从目标grant_id消耗
                i = 0
                while i < len(active_grants) and remaining_charge > 0:
                    expire_ts, available, gid = active_grants[i]
                    if gid == grant_id:
                        if available <= remaining_charge:
                            remaining_charge -= available
                            active_grants.pop(i)
                        else:
                            active_grants[i] = (expire_ts, available - remaining_charge, gid)
                            remaining_charge = 0
                    else:
                        i += 1
        
        return sum(amount for _, amount, gid in active_grants if gid == grant_id)
    
    def get_all_grants_balance(self, timestamp: int) -> dict:
        """Follow up 3: 获取所有grant的余额分布"""
        valid_events = [e for e in self.events if e[1] <= timestamp]
        valid_events.sort(key=lambda x: x[1])
        
        active_grants = []
        
        for event in valid_events:
            if event[0] == 'add':
                _, ts, amount, expire_ts, grant_id = event
                if expire_ts > timestamp:
                    heapq.heappush(active_grants, (expire_ts, amount, grant_id))
            elif event[0] == 'charge':
                _, ts, charge_amount = event
                remaining_charge = charge_amount
                
                temp_grants = []
                while active_grants and remaining_charge > 0:
                    expire_ts, available, grant_id = heapq.heappop(active_grants)
                    
                    if available <= remaining_charge:
                        remaining_charge -= available
                    else:
                        temp_grants.append((expire_ts, available - remaining_charge, grant_id))
                        remaining_charge = 0
                
                for grant in temp_grants:
                    heapq.heappush(active_grants, grant)
        
        # 按grant_id分组
        grant_balances = {}
        for expire_ts, amount, grant_id in active_grants:
            if expire_ts > timestamp:
                grant_balances[grant_id] = grant_balances.get(grant_id, 0) + amount
        
        return grant_balances

    def _calculate_balance(self, timestamp: int) -> int:
        """原始计算逻辑，允许负余额"""
        valid_events = [e for e in self.events if e[1] <= timestamp]
        valid_events.sort(key=lambda x: x[1])
        
        active_grants = []
        deficit = 0  # 记录超额使用
        
        for event in valid_events:
            if event[0] == 'add':
                _, ts, amount, expire_ts, grant_id = event
                if expire_ts > timestamp:
                    heapq.heappush(active_grants, (expire_ts, amount, grant_id))
            elif event[0] == 'charge':
                _, ts, charge_amount = event
                remaining_charge = charge_amount
                
                temp_grants = []
                while active_grants and remaining_charge > 0:
                    expire_ts, available, grant_id = heapq.heappop(active_grants)
                    
                    if available <= remaining_charge:
                        remaining_charge -= available
                    else:
                        temp_grants.append((expire_ts, available - remaining_charge, grant_id))
                        remaining_charge = 0
                
                # Follow up 4: 处理超额使用
                if remaining_charge > 0:
                    deficit += remaining_charge
                
                for grant in temp_grants:
                    heapq.heappush(active_grants, grant)
        
        total = sum(amount for expire_ts, amount, _ in active_grants if expire_ts > timestamp)
        return total - deficit

# 测试代码
if __name__ == "__main__":
    gpu = GPUSolution()
    
    # 基础测试
    gpu.add_credit('a', 100, 10, 30)
    gpu.charge(20, 15)
    
    try:
        print(f"Balance: {gpu.get_balance(20)}")  # 80
        print(f"Grant 'a' balance: {gpu.get_balance_by_grant('a', 20)}")  # 80
        print(f"All grants: {gpu.get_all_grants_balance(20)}")  # {'a': 80}
    except InsufficientCreditException as e:
        print(f"Error: {e}")
