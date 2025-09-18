
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        # TODO: Create a campaign on this channel and return an external id.
        raise NotImplementedError

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        # Attempt to allocate from the global budget
        GlobalBudget().allocate(campaign.daily_budget)
        # Return external id prefixed with 'g-'
        return f"g-{uuid4().hex[:8]}"

    def pause_campaign(self, campaign_id: str) -> None:
        # For exercise purposes, no-op
        return None

class FacebookAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        GlobalBudget().allocate(campaign.daily_budget)
        return f"f-{uuid4().hex[:8]}"

    def pause_campaign(self, campaign_id: str) -> None:
        return None

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
        if not isinstance(channel, str) or not channel:
            raise ValueError("Channel must be a non-empty string")
        key = channel.lower()
        if key == "google":
            return GoogleAdsClient("google")
        if key == "facebook":
            return FacebookAdsClient("facebook")
        raise ValueError(f"Unknown channel: {channel}")
