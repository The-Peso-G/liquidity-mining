from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class MiningRound(Base):
    __tablename__ = 'users'

    round = Column(String, primary_key=True)
    begin_block_number = Column(Integer)
    end_block_number = Column(Integer)
    watcher_id = Column(Integer)


class WatcherBlock(Base):
    __tablename__ = 'watcher_blocks'

    watcher_id = Column(Integer, primary_key=True)
    block_number = Column(Integer, primary_key=True)
    block_hash = Column(String)


class TokenEvent(Base):
    __tablename__ = "token_events"

    block_number = Column(Integer, primary_key=True)
    transaction_hash = Column(String, primary_key=True)
    event_index = Column(Integer, primary_key=True)
    token = Column(String, primary_key=True)
    holder = Column(String, primary_key=True)
    amount = Column(DECIMAL(78, 18))
    watcher_id = Column(Integer)


class TokenBalance(Base):
    __tablename__ = "token_balances"
    watcher_id = Column(Integer)
    token = Column(String)
    holder = Column(String)
    balance = Column(DECIMAL(78, 18))


class ImmatureMiningReward(Base):
    __tablename__ = "immature_mining_rewards"

    block_number = Column(Integer, primary_key=True)
    mining_round = Column(String, primary_key=True)
    holder = Column(String, primary_key=True)
    mcb_balance = Column(DECIMAL(78, 18))


class ImmatureMiningRewardSummary(Base):
    __tablename__ = "immature_mining_reward_summaries"

    mining_round = Column(String)
    holder = Column(String)
    mcb_balance = Column(DECIMAL(78, 18))


class MatureMiningReward(Base):
    __tablename__ = "mature_mining_reward"

    mining_round = Column(String)
    holder = Column(String)
    block_number = Column(Integer)
    mcb_balance = Column(DECIMAL(78, 18))


class MatureMiningRewardCheckpoint(Base):
    __tablename__ = "mature_mining_reward_checkpoints"
    mining_round = Column(String)
    holder = Column(String)
    block_number = Column(Integer)
    mcb_balance = Column(DECIMAL(78, 18))


class PaymentTransaction(Base):
    __tablename__ = "payment_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_nonce = Column(Integer)
    transaction_data = Column(String)
    transaction_hash = Column(String, nullable=True)
    status = Column(String, nullable=True)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    holder = Column(String)
    amount = Column(DECIMAL(78, 18))
    pay_time = Column(TIMESTAMP)
    transaction_id = Column(Integer, ForeignKey('payment_transactions.id'))
    payment_transaction = relationship(
        "PaymentTransaction", back_populates="payments")


class PaymentSummary(Base):
    __tablename__ = "payment_summaries"

    holder = Column(String)
    paid_amount = Column(DECIMAL(78, 18))


class RoundPayment(Base):
    __tablename__ = "round_payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    mining_round = Column(String)
    holder = Column(String)
    amount = Column(DECIMAL(78, 18))
    payment_id = Column(Integer, ForeignKey('payments.id'))
    payment = relationship("Payment", back_populates="round_payments")


class RoundPaymentSummary(Base):
    __tablename__ = "round_payment_summaries"

    mining_round = Column(String)
    holder = Column(String)
    paid_amount = Column(DECIMAL(78, 18))